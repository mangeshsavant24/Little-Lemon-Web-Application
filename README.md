# Little Lemon Web Application

Django + Django REST Framework app with HTML content, menu and table-booking APIs, registration/token authentication, and unit tests. MySQL is the default database.

## Setup (Windows PowerShell)
Use Python 3.11 or 3.12.

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Create the MySQL database:
```sql
CREATE DATABASE littlelemon CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

Set environment variables for your own MySQL credentials:
```powershell
$env:MYSQL_DATABASE="littlelemon"
$env:MYSQL_USER="root"
$env:MYSQL_PASSWORD="YOUR_MYSQL_PASSWORD"
$env:MYSQL_HOST="127.0.0.1"
$env:MYSQL_PORT="3306"
```

Run:
```powershell
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
Open `http://127.0.0.1:8000/`. Admin: `/admin/`.

For a smoke test without MySQL only, set `$env:DB_ENGINE="sqlite"` before migrations. Configure MySQL for final peer review.

## API endpoints
- `GET/POST /api/menu-items/`; detail operations at `/api/menu-items/<id>/`
- `GET/POST /api/categories/`; detail operations at `/api/categories/<id>/`
- `GET/POST /api/bookings/`; detail operations at `/api/bookings/<id>/`
- `POST /api/registration/` creates a user and returns a token
- `POST /api-token-auth/` obtains a token using username/password
- `GET /api/me/` returns current authenticated user
- `/api-auth/login/` browsable API login

Anonymous users can read APIs. Authenticated users can write menu/category data. Booking list/create supports anonymous or authenticated bookings.

## Insomnia checks
1. `GET http://127.0.0.1:8000/api/menu-items/`
2. `GET http://127.0.0.1:8000/api/bookings/`
3. Register: `POST /api/registration/`, JSON body:
   `{"username":"lemonuser","password":"SecurePass123","email":"lemon@example.com"}`
4. Token: `POST /api-token-auth/`, JSON body `{"username":"lemonuser","password":"SecurePass123"}`
5. Set header `Authorization: Token <token>`.
6. Create a category with `POST /api/categories/`, JSON `{"title":"Mains","slug":"mains"}`.
7. Create menu item with `POST /api/menu-items/`, JSON `{"title":"Lemon Pasta","price":"12.50","featured":true,"category_id":1}`.
8. Create booking with `POST /api/bookings/`, JSON `{"name":"Alex","no_of_guests":2,"booking_date":"2027-01-15T19:00:00+05:30"}`.
9. Test GET, PUT/PATCH, and DELETE on a detail URL.

## Tests
```powershell
python manage.py test
```

## GitHub submission
Create a repository on GitHub, then run from this directory:
```bash
git init
git add .
git commit -m "Build Little Lemon web application"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
git push -u origin main
```
Replace the placeholder with your real repository URL. Confirm files are pushed before submitting that URL to Coursera.
