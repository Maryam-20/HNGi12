# HNGi12
**Project Overview**

This project provides a simple public API that returns essential information in JSON format. The API delivers:

registered email address.

The current datetime as an ISO 8601 formatted timestamp.

The GitHub URL of the project's codebase.

** API Endpoint**

GET(http://127.0.0.1:8000/user_details/)

This endpoint returns JSON data with the following structure:

**Response Example**
{
  "id": "#",
  "objects_id": null,
  "content_type": null,
  "email_address": "name@gmail.com",
  "created_at": "2025-02-01T21:59:17.512390Z",
  "github_url": "https://github.com/username"
}

**Installation & Setup**

Follow these steps to set up and run the project locally.

1-  Clone the Repository
      git clone https://github.com/your-github-repo.git
      cd your-github-repo

2-  Create and Activate a Virtual Environment
       python -m venv venv
       
3-  Install Dependencies
        python install -r requirements.txt
        
4-  Run Database Migrations
      python manage.py makemigrations
      puthon manage.py migrate
      
5-  Start the Development Server
        python manage.py runserver
6-  Test the API
        URL: http://127.0.0.1:8000/user_details/
        
**Technologies Used**
Python
Django & Django Rest Framework
PostgreSQL



















