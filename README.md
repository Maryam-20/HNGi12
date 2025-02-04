# HNGi12
**Project Overview**

This project provides a simple public API that returns essential information in JSON format. The API delivers:

registered email address.

The current datetime as an ISO 8601 formatted timestamp.

The GitHub URL of the project's codebase.

** API Endpoint**

GET(https://hngi12-2025.onrender.com)

This endpoint returns JSON data with the following structure:

**Response Example**
{
  {
    "email": "maryamanileleye@gmail.com",
    "github_url": "https://github.com/Maryam-20/HNGi12",
    "current_datetime": "2025-02-04T21:27:14Z"
}
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
        URL: http://127.0.0.1:8000
        
**Technologies Used**
Python
Django & Django Rest Framework
PostgreSQL



















