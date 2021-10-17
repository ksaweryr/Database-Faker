#!/usr/bin/env python3

from dataclasses import astuple, dataclass
from datetime import datetime, date
from os import getenv
from random import choice, uniform

from dotenv import load_dotenv
from faker import Faker

from db import get_connector
from encrypt import encrypt


@dataclass
class Address:
	id: str
	city: str
	street: str
	building: int
	post_code: str


@dataclass
class CreditCard:
	id: str
	provider: str
	number: str
	cvv: int
	expire_date: date


@dataclass
class Customer:
	id: str
	first_name: str
	last_name: str
	password: str
	birth_date: date
	phone_number: str
	balance: float
	address_id: str
	credit_card_id: str


class DataGenerator(Faker):

	def __init__(self, *args, city_count=50, **kwargs):
		super().__init__(*args, **kwargs)
		self.cities = [self.unique.city() for _ in range(city_count)]

	def address(self):
		return Address(
			id = self.uuid4(),
			city = choice(self.cities),
			street = self.street_name(),
			building = self.building_number(),
			post_code = self.postcode()
		)

	def credit_card(self):
		return CreditCard(
			id = self.uuid4(),
			provider = self.credit_card_provider(),
			number = self.credit_card_number(),
			cvv = self.credit_card_security_code(),
			expire_date = datetime.strptime(
				self.credit_card_expire(),
				'%m/%y'
			).date()
		)

	def customer(self, address, credit_card):
		return Customer(
			id = self.uuid4(),
			first_name = self.first_name(),
			last_name = self.last_name(),
			password = encrypt(self.password()),
			birth_date = self.date_between(start_date='-70y', end_date='-20y'),
			phone_number = self.phone_number(),
			balance = round(uniform(500, 10_000), 2),
			address_id = address.id,
			credit_card_id = credit_card.id
		)

	def all(self):
		address = self.address()
		credit_card = self.credit_card()
		customer = self.customer(address, credit_card)
		return address, credit_card, customer


def load_query(name):
	with open(f'{getenv("RDBMS")}/queries/{name}.sql', 'rt') as f:
		return f.read()


def generate_data(d, c, queries):
	address, credit_card, customer = d.all()
	c.execute(
		queries['insert_address'],
		astuple(address)
	)
	c.execute(
		queries['insert_credit_card'],
		astuple(credit_card)
	)
	c.execute(
		queries['insert_customer'],
		astuple(customer)
	)


def main():
	load_dotenv(override=True)

	connection_args = {
		'host': getenv('HOST'),
		'port': getenv('PORT'),
		'database': getenv('DB'),
		'user': getenv('USER'),
		'password': getenv('PASSWORD'),
	}
	n = int(getenv('ROW_COUNT'))
	d = DataGenerator(city_count=int(getenv('CITY_COUNT')))

	queries = {
		name: load_query(name) for name in (
			'insert_address', 'insert_credit_card', 'insert_customer'
		)
	}

	with get_connector().connect(**connection_args) as conn:
		with conn.cursor() as c:
			for i in range(n):
				generate_data(d, c, queries)
				print(f'Generated {i + 1}/{n}')

		conn.commit()


if __name__ == '__main__':
	main()