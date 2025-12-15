# Bookly API

Bookly is a personal book-tracking REST API built with Django REST Framework.  
It allows users to manage books, track reading progress, and leave reviews.

## Features
- JWT authentication
- Book CRUD operations
- Reading status tracking
- Reviews and ratings
- Filtering and search

## Tech Stack
- Python
- Django
- Django REST Framework
- Simple JWT
- SQLite (development)

## API Endpoints

### Authentication
POST /api/token/

### Books
GET /api/books/  
POST /api/books/  
GET /api/books/{id}/  
PUT /api/books/{id}/  
DELETE /api/books/{id}/  

### Reading Status
POST /api/books/{id}/start_reading/  
POST /api/books/{id}/finish/  
POST /api/books/{id}/want_to_read/  
POST /api/books/{id}/drop/  

### Reviews
POST /api/books/{id}/review/  
GET /api/books/{id}/reviews/  

### Filtering
GET /api/books/?status=WANT  
GET /api/books/?search=harry  

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
