# DengueShield LK

## The problem

Sri Lanka faces recurring dengue outbreaks every year, worst during the rainy season. Health authorities rely mainly on manual field inspections to find mosquito breeding sites — stagnant water, discarded containers, blocked drains — but ordinary residents have no simple, fast way to report a breeding site themselves, or to check how risky their own area currently is.

## The solution

DengueShield LK lets residents report a suspected breeding site in under a minute, and see a live risk level — Low, Medium or High — for their own area, calculated from recent active reports. An AI assistant suggests the likely site type from the report description, and every report moves through a Reported → Verified → Cleared workflow so the data stays trustworthy.

## Tech stack

- **Frontend**: React (Vite), React Router, plain CSS
- **Backend**: FastAPI, SQLAlchemy, SQLite
- **AI**: Google Gemini (`gemini-1.5-flash`) for site-type suggestion, with a deterministic keyword-matching fallback that runs whenever the API key is missing or the call fails/times out

## AI usage declaration

This project uses AI in two ways:
1. **Build-time**: Claude Code was used to scaffold the FastAPI backend, React frontend, and seed data during development. All generated code was reviewed and the seed-data risk arithmetic was independently hand-verified before acceptance. See [AI_PROMPT_LOG.md](AI_PROMPT_LOG.md).
2. **Runtime feature**: the Report a Site form calls the Gemini API to suggest a site type from the free-text description. The suggestion is always shown to the reporter as an editable, overridable field — it is never auto-submitted. If Gemini is unavailable, a keyword-matching fallback (see `backend/app/ai_suggest.py`) guarantees the feature still works.

## Running locally (Windows / PowerShell)

### Backend

```powershell
cd backend
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item ..\.env.example .env
python scripts\seed_db.py
uvicorn app.main:app --reload --port 8000
```

The API runs at `http://localhost:8000` (interactive docs at `/docs`). `GEMINI_API_KEY` in `backend\.env` is optional — the app works fully without it via the keyword fallback.

### Frontend

```powershell
cd frontend
npm install
Copy-Item .env.example .env
npm run dev
```

The app runs at `http://localhost:5173`.

## Data model

Single entity: **Report** — `area` (one of 8 fixed areas), `site_type` (Blocked Drain / Discarded Tyre / Open Container / Water Tank / Construction Site / Other), `description` (required, ≥15 characters), `urgency` (Low / Medium / High, defaults to Medium), `reporter_contact` (optional), `status` (Reported → Verified → Cleared), `created_at`.

Note: `urgency` is reported by the resident and describes a single site. It is separate from an area's **risk level**, which is calculated from the number of active reports (see below).

## Risk formula

```
risk(area) = count of reports where status != Cleared AND created_at <= 30 days ago
  0–1 reports  → Low
  2–4 reports  → Medium
  5+  reports  → High
```

Sample areas: Wellawatte, Dehiwala, Kotte, Maharagama, Kaduwela, Negombo, Kandy Town, Galle Fort.

## Tests

```powershell
cd backend
.\venv\Scripts\Activate.ps1
pytest
```

<!-- Updated by Design Lead -->
