# Backend

Django + Django REST Framework API for the creator marketplace.

## What Phase 3 Adds

- Custom email-login user model stored in `users`.
- Django models matching `schema.sql` table names, foreign keys, uniqueness rules, and validation constraints.
- JWT access and refresh token endpoints with SimpleJWT.
- CRUD endpoints for every marketplace resource using DRF viewsets.
- OpenAPI schema and Swagger UI with drf-spectacular.

## Setup

```powershell
cd backend
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
copy .env.example .env
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

If `DATABASE_URL` is not set, Django uses a local SQLite database for development. For Neon or another PostgreSQL database, set `DATABASE_URL` in `.env`.

## Important URLs

- `POST /api/auth/token/` gets access and refresh JWTs.
- `POST /api/auth/token/refresh/` refreshes an access token.
- `GET /api/docs/` opens Swagger API docs.
- `GET /api/schema/` returns the OpenAPI schema.
- `GET /api/listings/` and the other `/api/*/` routes expose CRUD APIs.
