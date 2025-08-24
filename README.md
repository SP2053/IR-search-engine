# Sangram Poudel Scholar

FastAPI + vanilla JS vertical search over Coventry Pureportal publications.

## Dev
python -m venv .venv
. .venv/Scripts/activate  # or source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000

Open http://127.0.0.1:8000

## Data
The app reads `data/publications.json` (committed). Re-run the local crawler to refresh it, then commit & push.

## Deploy (DigitalOcean App Platform)
- Connect GitHub repo
- Autodetected as Python, uses Procfile
- No env vars required
- Add Custom Domain: www.ir.sangram.vse
