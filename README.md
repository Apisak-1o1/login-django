```markdown
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

```
login-django/
├── backend/      # Django backend (API)
├── frontend/     # Vue.js frontend
└── README.md
```

---

### Backend Setup

1. Create and activate a Python virtual environment:

   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate   # macOS/Linux
   venv\Scripts\activate      # Windows
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Apply migrations to create the database:

   ```bash
   python manage.py migrate
   ```

4. Run the Django development server:

   ```bash
   python manage.py runserver
   ```

---

### Frontend Setup

1. Navigate to the frontend folder:

   ```bash
   cd ../frontend
   ```

2. Install npm dependencies:

   ```bash
   npm install
   # or
   yarn install
   ```

3. Run the frontend development server:

   ```bash
   npm run dev
   # or
   yarn dev
   ```
```
