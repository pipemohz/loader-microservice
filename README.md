# File loader microservice
It's a web service that exposes an endpoint to read a file, query a series of MercadoLibre public APIs and upload the records to a database. It's based on the Python Flask framework and uses a database with the Postgres engine.

## Installation 🔧

Clone the repository in a your work folder.

## Configuration

### Prerequisites

* Python 3.10.x
* Docker engine
* [Postgres docker container](https://hub.docker.com/_/postgres/)
* Create a database in postgres for project

### Create a virtual environment
```sh
python -m venv .venv
```
### Activate virtual environment

#### Windows
```sh
.venv\Scripts\activate
```
#### Linux
```sh
source .venv/bin/activate
```
### Download all packages required
```sh
pip install -r requirements.txt
```
### Create an environment file

You must create and setting up an .env file for the project configuration with variables according to .env.example
```dosini
FLASK_APP=app.py
APP_ENV=development

DEBUG = True
TIMEZONE = America/Bogota

# Database settings
POSTGRES_URI =

#Supported formats
FORMATS=csv,txt,jsonl

# Mercadolibre settings
MULTIGET_MAX_ITEMS=20

# Mercadolibre APIs
MELI_ITEMS_API=
MELI_CATEGORIES_API=
MELI_CURRENCIES_API=
MELI_USERS_API=

# NO USED ON DEPLOYS [STAGING, PRODUCTION, QA]
# DATABASE_SETTINGS
POSTGRES_URI_TEST =

```
### Initialize migrations
```sh
flask db init
```
### Create new migrations
```sh
flask db migrate -m "Initial migration"
```
### Apply migrations
```sh
flask db upgrade
```
## Running tests
### Run app components tests
```sh
./run_tests.sh
```

## Deploy on local
### Run app components tests
```sh
python app.py
```
### Check the app is running on localhost
```sh
http://localhost:5000
```
```json
{
"message": "File loader service"
}
```