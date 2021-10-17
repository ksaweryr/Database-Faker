#!/usr/bin/env python3

from secrets import token_urlsafe


TEMPLATE = \
'''HOST=localhost
PORT=5050
DB=data
USER=user
PASSWORD={password}
ROW_COUNT=1000
CITY_COUNT=50
RDBMS=postgres # allowed: postgres, mysql
CREATE_CONTAINER=1

# Docker image and container name; only relevant if CREATE_CONTAINER != 0
IMAGE_NAME=fake_db
CONTAINER_NAME=fake_db_instance'''


def main():
	password = token_urlsafe(32)
	with open('.env', 'wt') as f:
		f.write(TEMPLATE.format(password=password))
	print('Successfully created .env file')


if __name__ == '__main__':
	main()