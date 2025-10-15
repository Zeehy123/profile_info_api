**Profile API Task

A simple RESTful API built with Django REST Framework that returns user profile information along with a random cat fact fetched dynamically from the Cat Facts API
.

This task demonstrates consuming third-party APIs, formatting JSON responses, and returning dynamic data in real-time.

---------------------------------------------------------------------------------------
🚀 Features

✅ GET /me endpoint that returns:
. status → Always "success"

. user → Your email, name, and backend stack

. timestamp → Current UTC time in ISO 8601 format

. fact → Random cat fact fetched from the Cat Facts API

✅ Handles external API errors gracefully
✅ Returns proper JSON content-type (application/json)
✅ Generates new data for each request

Example Response
{
  "status": "success",
  "user": {
    "email": "zainabyusuf@example.com",
    "name": "Zainab Yusuf",
    "stack": "Python/Django"
  },
  "timestamp": "2025-10-15T16:21:09.371Z",
  "fact": "Cats can rotate their ears 180 degrees."
}
-----------------------------------------------------------------------------------

⚙️ Tech Stack

. Language: Python 3.x

. Framework: Django + Django REST Framework

. HTTP Client: Requests

. Deployment: Railway.app

. Web Server: Gunicorn
----------------------------------------------------------------------------------

🛠️ Project Setup (Run Locally)
1. Clone the Repository
    git clone https://github.com/<your-username>/profile_info_api.git
  cd profile_info_api
2. Create & Activate Virtual Environment
   python -m venv venv
  source venv/bin/activate      
3. Install Dependencies
     pip install -r requirements.txt
4. Run Migrations
   python manage.py migrate
5. start the server
6. python manage.py runserver


---------------------------------------------------------------------------------
Test the API
Once the server is running visit
    GET http://127.0.0.1:8000/me
You’ll see a dynamic JSON response similar to the example above.

Each request returns:
. A new cat fact 🐈
.  fresh timestamp
. The same user info
