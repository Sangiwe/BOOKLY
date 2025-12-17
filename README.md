# Bookly API

Bookly is a personal book-tracking REST API built with Django REST Framework.  
It allows users to manage their personal library, track reading progress, and leave reviews on books they have read.

This project was built as a capstone project to demonstrate backend development skills, including authentication, RESTful API design, and deployment.

---

## Features
- JWT-based authentication
- User-specific book management (CRUD)
- Reading status tracking (want to read, reading, finished, dropped)
- Reviews and ratings
- Search and filtering
- Protected endpoints (authentication required)

---

## Tech Stack
- Python
- Django
- Django REST Framework
- Simple JWT
- SQLite (development)
- Deployed on PythonAnywhere

---

## Live API
Base URL:
          https://sangiwe7.pythonanywhere.com/api/


---

## Authentication

This API uses **JWT authentication**.

To access protected endpoints:
1. Obtain a token via:
                       POST /api/token/

2. Include the token in requests:
   Authorization: Bearer


Unauthorized requests will return:
 401 Unauthorized


---

## API Endpoints

### Authentication
- POST `/api/token/`

### Books
- GET `/api/books/`
- POST `/api/books/`
- GET `/api/books/{id}/`
- PUT `/api/books/{id}/`
- DELETE `/api/books/{id}/`

### Reading Status
- POST `/api/books/{id}/start_reading/`
- POST `/api/books/{id}/finish/`
- POST `/api/books/{id}/want_to_read/`
- POST `/api/books/{id}/drop/`

### Reviews
- POST `/api/books/{id}/review/`
- GET `/api/books/{id}/reviews/`

### Filtering & Search
- GET `/api/books/?status=WANT`
- GET `/api/books/?search=harry`

---

## Testing the API
The API can be tested using tools such as **Postman** or the **Django REST Framework browsable API**.  
Most endpoints require authentication.

---

## Setup Instructions

```bash
git clone https://github.com/Sangiwe/BOOKLY
cd BOOKLY
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
