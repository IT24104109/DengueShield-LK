# AI Prompt Log

Record every AI-tool interaction used while building DengueShield LK. One row per meaningfully distinct prompt.

| Tool | Exact prompt | Purpose | How checked / modified |
|---|---|---|---|
| Claude Code | (scaffold plan for DengueShield LK — see plan file) | Scaffold the full FastAPI + React app from the SE3090 brief | Reviewed generated seed-data arithmetic by hand (risk counts per area), corrected it before accepting; will review all generated code before demo |
| Gemini API (gemini-1.5-flash) | `You are classifying a mosquito breeding site report... Description: "{description}" Label:` (see `backend/app/ai_suggest.py`) | Runtime feature: suggest a `site_type` from the free-text report description | Verified fallback path (keyword matching) independently in `backend/tests/test_ai_suggest.py`; suggestion is always shown to the user as editable, never auto-submitted |

Add a new row every time a new prompt is used (e.g. About-page copywriting, demo script drafting, README polish).
