"# login-django" 
# Login-Django-Vue

A simple user authentication system with Django REST API backend and Vue.js + TailwindCSS frontend.

---

## Features

- User Sign Up with username, first name, last name, email, and password
- User Sign In with session authentication
- User Sign Out
- API communication between frontend and backend using Django REST Framework
- Clean UI with TailwindCSS

---

## Project Structure

login-django/
├── backend/ # Django backend (API)
├── frontend/ # Vue.js frontend
└── README.md

### Backend
1. Create and activate a Python virtual environment:

cd backend
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows

2. Install dependencies:
pip install -r requirements.txt

3. Apply migrations to create the database:
python manage.py migrate

4. Run the Django development server:
python manage.py runserver

### Frontend
1. Navigate to the frontend folder:
cd ../frontend
2. cd ../frontend
Install npm dependencies:
3. Run the frontend development server:
npm run dev
# or
yarn dev