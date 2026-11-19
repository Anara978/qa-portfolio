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
- [recruit-e2e-v2.postman_collection.json](recruit-e2e-v2.postman_collection.json) — End-to-end API testing collection created in Postman.


## Recruit E2E API Testing — Postman

[View the Postman collection](recruit-e2e-v2.postman_collection.json)

An end-to-end REST API testing workflow for a recruitment system using Postman. The collection covers candidate and recruiter authentication, position and application lifecycle operations, response validation, and environment-variable management.

### End-to-End Flow

1. Register a candidate and log in
2. Log in as a recruiter and create a position
3. Submit an application
4. Update the position and verify it with GET by ID
5. Delete the application
6. Verify the active candidate token (positive test)
7. Log out and verify the old token is rejected with HTTP 401 (negative test)
8. Log in again and delete the candidate
9. Delete the position

### Automated Checks

- HTTP status codes and response-body validation
- JSON schema and returned-field validation
- Dynamic IDs shared between dependent requests
- Bearer-token authentication and logout verification
- Cleanup of temporary test data

### Collection Runner Results

| Metric | Result |
| --- | --- |
| Run date | November 19, 2026 |
| Collection requests | 14 |
| Automated tests | 116 passed (reported from local Postman run) |
| Execution time | Approximately 1 second |
| Execution | Postman Collection Runner, environment `e2e` |

The run results above were reported from Postman; the separate Runner report is not included in this repository.

### Running the Collection

Import the collection into Postman and configure an `e2e` environment with `baseURL`, `candidatePassword`, `recruiterEmail`, and `recruiterPassword`. Request scripts generate and store the temporary candidate, position, application, and token variables used throughout the flow.

Credentials and live authentication tokens are **not included** in the published collection.

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

### Image Upload Troubleshooting
Tools: Postman, Swagger Petstore API v3

This project demonstrates my hands-on practice in API testing, including creating, updating, and deleting pet records, working with request parameters, authentication, and validating API responses.

While testing the POST /pet/{petId}/uploadImage endpoint, I investigated several unsuccessful requests.

#### Issues investigated:

- 415 Unsupported Media Type — investigated request body formats and Content-Type headers.

- 404 Pet not found — checked whether the target pet record existed before uploading an image.

#### Steps taken:

- Inspected request and response details using Postman Console.

- Compared form-data and binary request formats.

- Configured API Key authentication.

- Updated the Content-Type settings.

- Recreated the pet record and repeated the image upload test.

#### Key Learning

This exercise helped me understand how API requests depend on correct data formats, request headers, authentication, and existing server-side records.

It also reinforced the importance of investigating the root cause of an error rather than repeatedly changing request settings without verifying the results.
