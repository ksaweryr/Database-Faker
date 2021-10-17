#!/bin/bash

if [ ! -e .env ]
then
	python3 setup_dotenv.py
fi

if [ ! -e venv ]
then
	python3 -m virtualenv venv
fi

source venv/bin/activate
pip install -U pip
pip install -r requirements.txt