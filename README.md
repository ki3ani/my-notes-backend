# My Notes App API Documentation

Welcome to the API documentation for My Notes App. This document provides detailed information about the available API endpoints, authentication, request and response formats, and error handling.

## Base URL

All API endpoints are relative to the base URL of your backend server. The base URL for the My Notes App API is `https://api.my-notes-app.com`.

## Authentication

Authentication is required to access certain endpoints. The API uses token-based authentication. To authenticate a request, include an `Authorization` header with a valid JWT token.

Example:

```http
Authorization: Bearer <JWT_TOKEN>
