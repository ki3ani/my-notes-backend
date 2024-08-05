# My Notes App API Documentation

Welcome to the API documentation for My Notes App. This document provides detailed information about the available API endpoints, authentication, request and response formats, and error handling.



## Authentication

Authentication is required to access certain endpoints. The API uses token-based authentication. To authenticate a request, include an `Authorization` header with a valid JWT token.

Example:

```http
Authorization: Bearer <JWT_TOKEN>
```

## Endpoints

### User Registration

- **Endpoint**: `/api/auth/register`
- **Method**: POST
- **Description**: Register a new user account.
- **Request Body**:
  - `username` (string, required): The username of the new user.
  - `email` (string, required): The email address of the new user.
  - `password` (string, required): The password for the new account.
- **Response**:
  - `message` (string): A success message upon successful registration.

### User Login

- **Endpoint**: `/api/auth/login`
- **Method**: POST
- **Description**: Log in with an existing user account.
- **Request Body**:
  - `email` (string, required): The email address of the user.
  - `password` (string, required): The user's password.
- **Response**:
  - `token` (string): A JWT token for authentication.
  - `user` (object): User information.

### Create Note

- **Endpoint**: `/api/notes`
- **Method**: POST
- **Description**: Create a new note.
- **Request Body**:
  - `title` (string, required): The title of the note.
  - `content` (string, required): The content of the note.
- **Response**:
  - `id` (integer): The unique identifier of the created note.
  - `title` (string): The title of the note.
  - `content` (string): The content of the note.
  - `user_id` (integer): The ID of the user who created the note.
  - `created_at` (string): Timestamp of when the note was created.

### Get Notes

- **Endpoint**: `/api/notes`
- **Method**: GET
- **Description**: Retrieve a list of all user's notes.
- **Response**:
  - An array of note objects, each containing `id`, `title`, `content`, `user_id`, and `created_at` fields.

### Update Note

- **Endpoint**: `/api/notes/:id`
- **Method**: PUT
- **Description**: Update an existing note.
- **Request Body**:
  - `title` (string, required): The updated title of the note.
  - `content` (string, required): The updated content of the note.
- **Response**:
  - `message` (string): A success message upon successful update.

### Delete Note

- **Endpoint**: `/api/notes/:id`
- **Method**: DELETE
- **Description**: Delete a note by its ID.
- **Response**:
  - `message` (string): A success message upon successful deletion.

## Error Handling

The API may return error responses with appropriate HTTP status codes. Error responses will include a `message` field with a description of the error.

**Example error response**:

```json
{
  "message": "User not found"
}
```
