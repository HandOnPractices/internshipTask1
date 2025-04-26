# Health System
- Health System is a Django-based web application for managing health programs and client information, with a RESTful API and Bootstrap-powered frontend.

## Features
- Health Program Management: Create, view, update, delete health programs.

- Client Management: Register, search, view client profiles and associated programs.

- Django Admin Interface: Manage programs, clients, and users.

- RESTful API: Public API endpoints for health programs and clients.

- Responsive Design: Bootstrap 5.3.3 frontend.

- Database: MySQL.

- Tech Stack: Django 4.x, Django REST Framework, Python 3.13, Git.

## Installation
- Clone the Repository:
- git clone https://github.com/HandOnPractices/internshipTask1.git
- cd internshipTask1
## Set Up Virtual Environment:
- python -m venv myenv
####  To activate the virtual environment
- source myenv/bin/activate  
### Windows: 
- myenv\Scripts\activate
###Install Dependencies:
- pip install django djangorestapi
#### Configure MySQL Database:
- Update health_system/settings.py:

`DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'health_system_db',
        'USER': 'your_mysql_user',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}`
#### Apply Migrations & Create Superuser:
`
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
Run Server:
`
### Start the server
`python manage.py runserver`
Usagw
`
Frontend Home: http://127.0.0.1:8000/clients/
`
`
Admin Panel: http://127.0.0.1:8000/admin/
`
### API Endpoints Example:
`
GET /clients/api/programs/ (List Programs)
`
`
POST /clients/api/programs/ (Create Program)
`
`
GET /clients/api/clients/ (List Clients)
`


#### Project Structure
`
health-system/
├── clients/            # App (models, views, templates, serializers)
├── health_system/      # Project settings and URLs
├── manage.py
├── requirements.txt
└── README.md
Troubleshooting
`
- MySQL errors: Check server status and credentials.

- Migration issues: Delete migrations folder and re-run migrations.

- Admin login issues: Reset superuser password if needed.
