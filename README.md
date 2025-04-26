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
### Install Dependencies:
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

## Homepage
  ![image](https://github.com/user-attachments/assets/4d21d41c-0cb4-4010-9342-63b2de8db84b)
## Create Program page
![image](https://github.com/user-attachments/assets/6a3143b5-b525-4f4f-bf40-bc08484c67c0)

- Program successfully created
![image](https://github.com/user-attachments/assets/643444b7-7146-441b-a990-2e743b97056e)
## Register a client and add to a program
![image](https://github.com/user-attachments/assets/8437e999-818d-49cb-81e1-59011dfc672d)

## Search For Client
![image](https://github.com/user-attachments/assets/06a8e233-0927-4a2e-a846-b08bb40ceae1)
- search implemented
  ![image](https://github.com/user-attachments/assets/aff4d436-c0d2-493f-b0ce-fafc3361133a)
### API END POINTS
- programs
![image](https://github.com/user-attachments/assets/b39f58bb-8110-45db-9114-e60ff7fa4939)
- clients
  ![image](https://github.com/user-attachments/assets/1b63921e-47c2-40b0-bf6b-8a2e424d4c23)
- API TEST USING CURL
  ![image](https://github.com/user-attachments/assets/50070c15-6e10-46d7-9af1-b173652c92c0)


