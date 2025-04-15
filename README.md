Django Projects

project - 03_simpleqna

A simple web-based Question & Answer platform built with Django, where authenticated users can:
- Ask questions
- Post answers (except to their own questions)
- Upvote answers
- View answers to questions

---

## Features

- User Authentication
- Ask Questions
- Answer Questions
- Edit Your Answer
- Upvote / Remove Upvote
- Show total upvotes per answer
- Login required to interact
- Basic CSRF protection
- Cache control decorators to prevent stale data

---

## Tech Stack

- Python 3.x
- Django 5.x
- SQLite3 (default, can be switched)
- HTML5, CSS3 (for frontend)
- JavaScript (for AJAX upvotes)

---

## Getting Started

### Prerequisites

- Python 3.8+
- pip (Python package installer)
- Django 5+
- Git

### Installation



pip install -r requirements.txt

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create a superuser (optional)
python manage.py createsuperuser

# Run the server
python manage.py runserver