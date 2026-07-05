# Free Deployment Guide

Your PC is not used as the public server. The public site runs on Vercel, the API runs on Render, the database runs on Neon, and uploads run on Cloudinary.

## 1. Neon Postgres

1. Go to `https://neon.tech`.
2. Sign in with GitHub or email.
3. Click **New Project**.
4. Choose the free plan and the closest region.
5. Copy the pooled connection string. It becomes `DATABASE_URL` in Render.

## 2. Cloudinary

1. Go to `https://cloudinary.com`.
2. Create a free account.
3. Open **Dashboard**.
4. Copy `Cloud name`, `API key`, and `API secret`.
5. Add them to Render as `CLOUDINARY_CLOUD_NAME`, `CLOUDINARY_API_KEY`, and `CLOUDINARY_API_SECRET`.

## 3. GitHub

1. Create an empty GitHub repository.
2. Push this project to that repository.
3. Use that repository for both Render and Vercel.

I must ask you which GitHub account/repository to use before I publish.

## 4. Render Backend

1. Go to `https://render.com`.
2. Click **New +** then **Web Service**.
3. Connect the GitHub repository.
4. Use:
   - Root directory: `backend`
   - Build command: `pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate`
   - Start command: `gunicorn config.wsgi:application`
5. Add environment variables from `backend/.env.example`.
6. Set `DJANGO_DEBUG=False`.
7. Set `DJANGO_ALLOWED_HOSTS` to your Render domain, for example `creator-marketplace-backend.onrender.com`.

## 5. Vercel Frontend

1. Go to `https://vercel.com`.
2. Click **Add New Project**.
3. Import the same GitHub repository.
4. Set root directory to `frontend`.
5. Add `NEXT_PUBLIC_API_URL` with your Render backend URL ending in `/api`.
6. Deploy.

## 6. Connect Frontend and Backend

After Vercel gives a public URL, add it to Render:

```text
CORS_ALLOWED_ORIGINS=https://your-site.vercel.app
CSRF_TRUSTED_ORIGINS=https://your-site.vercel.app
```

Then redeploy Render.
