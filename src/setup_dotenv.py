#!/usr/bin/env python3

from secrets import token_urlsafe


TEMPLATE = \
'''HOST=localhost # RDBMS host
PORT=5050 # RDBMS port
DB=data # Database name
USER=user # Username
PASSWORD={password} # Password
ROW_COUNT=1000 # Number of rows to insert
CITY_COUNT=50 # Number of city names to generate
RDBMS=postgres # RDBMS; allowed: postgres, mysql
CREATE_CONTAINER=1 # 0 if database already exists; 1 if a Docker container should be created

# Docker image and container name; only relevant if CREATE_CONTAINER != 0
IMAGE_NAME=fake_db # Name of Docker image
CONTAINER_NAME=fake_db_instance # Name of Docker container'''


def main():
	password = token_urlsafe(32)
	with open('.env', 'wt') as f:
		f.write(TEMPLATE.format(password=password))
	print('Successfully created .env file')


if __name__ == '__main__':
	main()