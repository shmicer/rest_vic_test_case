# DRF QUIZ API

A simple Django Rest Framework application for unique quiz question receive.


## Description

- There are number of questions in POST-request;
- After POST-request a unique question  haas been saved to a database;
- If the question is not unique  request data from the public API until the question is unique;


## Tech stack

- Django
- Django REST Framework
- PostgreSQL
- Docker


## Installation

1. Clone the repository: `git clone https://github.com/shmicer/rest_vic_test.git`
2. Navigate to the project directory: `cd rest_vic_test_case`
3. Rename the `.env.django.example` and `.env.postgres.example` files found in the root directory of the project to 
folder `.envs/local/.django`, `.envs/local/.postgres` and update the environment variables accordingly.
4. Then you can start the project using Docker or manually using virtual environment.

Using Docker:

```
$ docker compose -f local.yml build

$ docker compose -f local.yml up

```
Run the following command to make migrations:

```
$ docker-compose -f local.yml exec web python3 manage.py makemigrations 

$ docker-compose -f local.yml exec web python3 manage.py migrate
```

Open a browser and go to http://localhost:8000

### Create a POST response:

###### Required parameters
``questions_num``  - Number of questions to request from API service

 
###### Endpoint

POST /api/

###### Example request
```
curl -X 'POST' \
  'http://0.0.0.0:8000/api/' \
  -H 'accept: */*' \
  -H 'Content-Type: application/json' \
  -H 'X-CSRFTOKEN: 8lCWex5xK6vfRoiS0A5dnjSzmt9IODZxJ5EVQLJ2P9WLxnNsbW920Uyg01YcCidq' \
  -d '{
  "questions_num": 3
}'
```
###### Example JSON response
```
{
  "question_id": 57413,
  "text": "Michael,Shirley,Jesse",
  "answer": "Jackson",
  "created": "2022-12-30T19:02:12.891000Z"
}
```

## Connect to PostgreSQL:

```
$ To conect to your databese you can use any PostgreSQL client (for example, psql or GUI-cluent, 
such as pgAdmin od DBeaver).

$ You data to connect to database is in .envs/local/.postgres file.

$ psql -h localhost -p 5432 -U username -d database_name
```


## API Documentation

Our API is documented using OpenAPI. You can view the full API schema by clicking the link below:

[OpenAPI Schema](./schema.yaml)

The docs are available at http://localhost:8000/api/docs





