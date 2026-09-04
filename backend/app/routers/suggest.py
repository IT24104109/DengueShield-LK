from fastapi import APIRouter

from ..ai_suggest import suggest_site_type
from ..schemas import SuggestRequest, SuggestResponse

router = APIRouter()


@router.post("/suggest-site-type", response_model=SuggestResponse)
def suggest(payload: SuggestRequest):
    site_type, source = suggest_site_type(payload.description)
    return SuggestResponse(suggested_site_type=site_type, source=source)
