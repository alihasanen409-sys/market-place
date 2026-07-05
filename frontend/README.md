# Frontend

Next.js App Router frontend for Creator Market.

## Features

- English and Arabic interface with RTL support.
- Simple responsive marketplace, product, dashboard, auth, cart, checkout, chat, and policy pages.
- React Query API integration with safe fallback listings for first deployment.
- Light and dark theme toggle.
- Low-RAM build setting: Next build workers are limited to 2 in `next.config.js`.

## Setup

```powershell
cd frontend
npm install
copy .env.example .env.local
npm run build
```

Set `NEXT_PUBLIC_API_URL` to your Render backend URL plus `/api`, for example:

```text
https://creator-marketplace-backend.onrender.com/api
```
