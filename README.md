# crudAPI

This is a simple CRUD API built using FastAPI, a modern, fast, and lightweight Python web framework. It allows users to create, read, update, and delete resources via HTTP requests.

#Prerequisites
```
Python 3.7 or later
FastAPI 0.61.1 or later
Other dependencies are listed in requirements.txt
Installation
Clone the repository
Install the dependencies: pip install -r requirements.txt
Run the development server: uvicorn main:app --reload
```
#Endpoints
The API has the following endpoints:
```
GET /api/v1/users/id/{user_id}: retrieves a specific user by user_id
GET /api/v1/users/email/{email}: retrieves a specific user by email
POST /api/v1/users: create a user
DELETE /api/v1/users/email/{user_email}: deletes a specific user by email
DELETE /api/v1/users/id/{user_id}: deletes a specific user by user_id
PUT /api/v1/users/update/{id_}: updates a specific user by id
PUT /api/v1/users/deactivate/{id_}: deactivate specific user by id

GET /api/v1/posts/{id_}: retrieves a specific post by user_id
POST /api/v1/posts: create a post
DELETE /api/v1/posts/{id_}: deletes a specific post by id_
PUT /api/v1/posts/{id_}: updates a specific post by id

POST /api/v1/token: authenticate using password and username, get token as response 
```
