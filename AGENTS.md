# Product Store Agent Context

## Project
Simple Flask CRUD API with a single HTML frontend. No build step. No framework.

## Stack
- Backend: Python, Flask, flask-cors
- Frontend: Plain HTML, CSS, vanilla JS
- Storage: In-memory dict, no database

## API Endpoints
- GET /products
- POST /products
- GET /products/<id>
- PUT /products/<id>
- DELETE /products/<id>

## Rules
- Keep frontend as a single HTML file
- No npm, no React, no build tools
- All validation happens in the Flask backend
- Do not add a database unless explicitly asked