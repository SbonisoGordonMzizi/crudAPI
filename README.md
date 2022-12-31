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
GET /resources: retrieves a list of all resources
POST /resources: creates a new resource
GET /resources/{id}: retrieves a specific resource by id
PUT /resources/{id}: updates a specific resource by id
DELETE /resources/{id}: deletes a specific resource by id
```

#Example Usage
Here is an example of how to use the API with curl:

Copy code
# Retrieve a list of resources
curl http://localhost:8000/resources

# Create a new resource
curl -X POST -d '{"name": "resource1"}' http://localhost:8000/resources

# Retrieve a specific resource
curl http://localhost:8000/resources/1

# Update a specific resource
curl -X PUT -d '{"name": "resource2"}' http://localhost:8000/resources/1

# Delete a specific resource
curl -X DELETE http://localhost:8000/resources/1
