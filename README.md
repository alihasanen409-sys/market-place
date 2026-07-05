# Marketplace Project

A full-stack creator marketplace for digital products and creative services.

- **Frontend:** Next.js + TypeScript + Tailwind CSS
- **Backend:** Django + Django REST Framework
- **Database:** PostgreSQL on Neon free tier
- **Auth:** JWT access and refresh tokens
- **File storage:** Cloudinary free plan
- **Hosting:** Vercel frontend + Render backend

## Repo Structure

```text
marketplace/
├── backend/     # Django + DRF API
├── frontend/    # Next.js app
├── docs-api.md
├── docs-deployment.md
├── docs-user-guide.md
└── README.md
```

## Status

Built through Phase 9. The app is ready for cloud deployment after GitHub,
Neon, Render, Vercel, and Cloudinary accounts are connected.

## Phases

- [x] Phase 1: Project skeleton
- [x] Phase 2: Database design (ERD + schema)
- [x] Phase 3: Backend core (models, JWT auth, CRUD)
- [x] Phase 4: Backend extras (search, uploads, reviews, messaging)
- [x] Phase 5: Frontend pages
- [x] Phase 6: Security pass
- [x] Phase 7: Testing
- [x] Phase 8: Deployment
- [x] Phase 9: Documentation

## Local Verification

Backend:

```powershell
cd backend
.venv\Scripts\python manage.py check
.venv\Scripts\python -m pytest
```

Frontend:

```powershell
cd frontend
npm test -- --runInBand
npm run build
```

## Documentation

- Backend setup: `backend/README.md`
- Frontend setup: `frontend/README.md`
- Deployment guide: `docs-deployment.md`
- API guide: `docs-api.md`
- User/admin guide: `docs-user-guide.md`
