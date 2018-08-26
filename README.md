# Circus - A API example using Eve Python
This is a simple example how to use Eve (http://python-eve.org/) to build a API Restful that made a user score managment. This API use JWT to authenticate.

## Data relations
One User can have one or more scores.

## Requisites
* A mongoDB up running;
* Configuration set up in the file `env.py`. The most important configurations are:

  * mongo connection string;
  * JWT secret key;
  * Application port
  * Permission key.

## Starting application
* Install requirements
* run `python app.py`

## Authentication
To get the token, you will need a make a POST request to `localhost/auth/token` with the body:

```
{
    "permission_key": "123456"
}
```
Go to the file `env.py` to change the key.

## Routes
### Protected with JWT:
* /users
* /scores
### Public
* /auth/token
* /healthcheck