# Library-Management-System

## Create virtual environment and activate
### `python3 -m virtualenv venv`
### `source venv/bin/activate`

## Install dependencies
### `pip install -r requirements.txt`

## Copy .env.example to .env and configure .env
### `cp .env.example .env`

## Setup Database and Run migrations
### `python manage.py migrate`

## Run server
### `python manage.py runserver`

# For Docker

## Copy .env.example to .env and configure .env
### `cp .env.example .env`

## Build and run containers
### `docker-compose up --build`

## Apply database migrations
### `docker-compose exec web python manage.py migrate`

## Create superuser
### `docker-compose exec web python manage.py createsuperuser`