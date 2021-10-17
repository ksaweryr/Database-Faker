from os import getenv


def get_connector():
	rdbms = getenv('RDBMS')

	if rdbms == 'postgres':
		import psycopg2, psycopg2.extras

		return psycopg2
	elif rdbms == 'mysql':
		import mysql.connector

		return mysql.connector
	else:
		raise ValueError(f'Unsupported RDBMS: {rdbms}')