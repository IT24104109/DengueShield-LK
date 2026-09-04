import httpx

from .config import GEMINI_API_KEY
from .models import SiteType

GEMINI_URL = (
    "https://generativelanguage.googleapis.com/v1beta/models/"
    "gemini-1.5-flash:generateContent"
)
TIMEOUT_SECONDS = 4.0

PROMPT_TEMPLATE = """You are classifying a mosquito breeding site report for a dengue-prevention app in Sri Lanka.
Given the description below, respond with EXACTLY ONE of these six labels, nothing else:
Blocked Drain
Discarded Tyre
Open Container
Water Tank
Construction Site
Other

Description: "{description}"
Label:"""


def keyword_fallback(description: str) -> SiteType:
    """Deterministic classifier used whenever the Gemini call is unavailable.

    Checked most-specific first so "discarded tyres and bottles" resolves to
    Discarded Tyre rather than Open Container.
    """
    text = description.lower()
    if any(k in text for k in ("tyre", "tire")):
        return SiteType.DISCARDED_TYRE
    if any(k in text for k in ("tank", "barrel", "sump")):
        return SiteType.WATER_TANK
    if any(k in text for k in ("drain", "gutter", "canal")):
        return SiteType.BLOCKED_DRAIN
    if any(k in text for k in ("construction", "building site", "scaffold")):
        return SiteType.CONSTRUCTION_SITE
    if any(k in text for k in ("bottle", "container", "bucket", "pot", "can")):
        return SiteType.OPEN_CONTAINER
    return SiteType.OTHER


def _parse_gemini_label(text: str) -> SiteType | None:
    lowered = text.strip().lower()
    for site_type in SiteType:
        if site_type.value.lower() in lowered:
            return site_type
    return None


def suggest_site_type(description: str) -> tuple[SiteType, str]:
    """Returns (SiteType, source) where source is 'gemini' or 'fallback'. Never raises."""
    if not GEMINI_API_KEY:
        return keyword_fallback(description), "fallback"

    try:
        payload = {
            "contents": [
                {"parts": [{"text": PROMPT_TEMPLATE.format(description=description)}]}
            ]
        }
        response = httpx.post(
            GEMINI_URL,
            params={"key": GEMINI_API_KEY},
            json=payload,
            timeout=TIMEOUT_SECONDS,
        )
        response.raise_for_status()
        data = response.json()
        text = data["candidates"][0]["content"]["parts"][0]["text"]
        label = _parse_gemini_label(text)
        if label:
            return label, "gemini"
        return keyword_fallback(description), "fallback"
    except Exception:
        return keyword_fallback(description), "fallback"
