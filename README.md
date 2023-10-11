# DRF Training System

A simple Django Rest Framework application for training system.


## Description

- There are list of available lessons for user;
- User have a list of products available for him;
- User can retrieve product information with a details such as status of view, 
view time and the last view date of lesson;
- Admin can retrieve the summary of product information: number of users, total viewed lessons,
total time of view in seconds, percentage of buying this product.

## Installation

1. Clone the repository: `git clone https://github.com/shmicer/rest_vic_test.git`
2. Navigate to the project directory: `cd training_system_test_case`
3. Rename the `.env.django.example` and `.env.postgres.example` files found in the root directory of the project to 
folder `.envs/local/.django`, `.envs/local/.postgres` and update the environment variables accordingly.
4. Then you can start the project using Docker or manually using virtual environment.

Using Docker:

```
$ docker compose -f local.yml build

$ docker compose -f local.yml up

```


Open a browser and go to http://localhost:8000


## API Documentation

Our API is documented using OpenAPI. You can view the full API schema by clicking the link below:

[OpenAPI Schema](./schema.yaml)

[//]: # (### Endpoints)

[//]: # ()
[//]: # (#### 1. Retrieve List of Lessons)

[//]: # ()
[//]: # (- **URL:** `/api/lessons/`)

[//]: # (- **Method:** `GET`)

[//]: # (- **Description:** Retrieve a list of all lessons for authenticated user with a status of view.)

[//]: # (- **Parameters:** None)

[//]: # (- **Response:**)

[//]: # (  - Status Code: 200 OK)

[//]: # (  - Body: JSON array of lessons.)

[//]: # ()
[//]: # (#### 2. Retrieve Product List)

[//]: # ()
[//]: # (- **URL:** `/api/products/`)

[//]: # (- **Method:** `GET`)

[//]: # (- **Description:** Return a list of all products for authenticated user.)

[//]: # (- **Parameters:** None)

[//]: # (- **Response:**)

[//]: # (  - Status Code: 200 OK)

[//]: # (  - Body: JSON array of lessons.)

[//]: # ()
[//]: # (#### 3. Retrieve Product Lessons)

[//]: # ()
[//]: # (- **URL:** `/api/products/{product_id}/`)

[//]: # (- **Method:** `GET`)

[//]: # (- **Description:** Retrieve lessons for a specific product.)

[//]: # (- **Parameters:**)

[//]: # (  - `{product_id}`: ID of the product.)

[//]: # (- **Response:**)

[//]: # (  - Status Code: 200 OK)

[//]: # (  - Body: JSON object with product lessons.)

[//]: # ()
[//]: # (#### 3. Retrieve Product Summary)

[//]: # ()
[//]: # (- **URL:** `/api/summary/{product_id}/`)

[//]: # (- **Method:** `GET`)

[//]: # (- **Description:** Retrieve details for a specific product.)

[//]: # (- **Parameters:**)

[//]: # (  - `{product_id}`: ID of the product.)

[//]: # (- **Response:**)

[//]: # (  - Status Code: 200 OK)

[//]: # (  - Body: JSON object with product summary.)

# rest_vic_test
