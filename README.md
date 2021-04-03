# client

## Local Project setup
```
pip install -r requirements.txt
```

### install pipenv
```
pip install pipenv
```

### create the virtual environment for the project
```
pipenv --three
```

### start virtual environment
```
pipenv shell
```

### Add dependencies
```
pipenv install
```
#### * flask - Flask is a microframework for Python based on Werkzeug, Jinja 2 and good intentions

#### * flask sqlalchemy - flask wrapper for Sqlalchemy, it adds Sqlalchemy support to flask apps

#### * psycopg2 - python postgresql adapter that provides some commands for simple CRUD queries and more on postgresql db

#### * flask-migrate - flask extension that handles SQLAlchemy database migration. Migration basically refers to #the management of incremental, reversible changes to relational database schemas

#### * flask-script - provides an extension for managing external scripts in flask. This is needed in running our #db migrations from the command line

#### * marshmallow - marshmallow is a library for converting complex datatypes to and from native Python datatypes. Simply put it is used for deserialization(converting data to application object) and serialization(converting application object to simple types).

#### * python-dotenv - For using the env variables.

### change the environment variable such as
```
SQLALCHEMY_DATABASE_URI=postgresql://<user>:<password>@<server_address>:<port_number>/<db_name>

e.g, SQLALCHEMY_DATABASE_URI=postgresql://tanuj:password@localhost:5432/createurad
```

### Migrate the Database
```
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
```

### Start the application
```
python run.py
```
