# URL Shortener with Analytics

Minimal full-stack scaffold. MongoDB access is confined to the FastAPI backend. The frontend currently contains placeholder routes only.

## Requirements

- Node.js and npm
- Python 3.10+
- MongoDB running at the URL configured in `backend/.env`

To run a local MongoDB with Docker, if needed:

```powershell
docker run --name url-shortener-mongo -p 27017:27017 -d mongo:8
```

## Start the backend

From the project root in PowerShell:

```powershell
cd backend
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
uvicorn app.main:app --reload
```

The API is available at `http://localhost:8000`; its health check is `http://localhost:8000/health`.

## Start the frontend

In a second terminal from the project root:

```powershell
cd frontend
npm install
npm run dev
```

Open `http://localhost:3000`. The frontend API base URL is configured in `frontend/.env.local`.

## Environment variables

Backend settings are in `backend/.env`; frontend settings are in `frontend/.env.local`. Example files are included for reference. Replace local values as needed; do not commit real credentials.