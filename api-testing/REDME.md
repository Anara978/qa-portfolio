# API Testing

This folder contains my API testing practice projects.

## Tools
- Postman
- Swagger
- Environment Variables
- Bearer Token Authentication
- Response Validation
- End-to-End API Flows

## Practice
- Candidate registration
- Candidate login
- Recruiter login
- Create and update position
- Create and delete application
- Logout and token verification

## Project Files
- recruit-e2e-v2.postman_collection.json`
— End-to-end API testing collection created in Postman.


## Swagger Petstore API Project

This project demonstrates end-to-end API testing using Swagger Petstore and Postman.

### Flow
- Create Pet
- Upload Pet Image
- Update Pet
- Delete Pet
- Verify Pet Deletion

### Validation
- Response schema validation
- Status code checks
- Response body validation
- Environment variables
- Dynamic petId handling
- Binary file upload testing

### Notes
Image upload was tested manually using a local binary file. The request works successfully in Postman, while Collection Runner requires access to the local file.

### Project Files
- `swagger-petstore.postman_collection.json`
- `petstore.postman_environment.json`
