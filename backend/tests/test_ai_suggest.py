from app.ai_suggest import keyword_fallback, suggest_site_type
from app.models import SiteType


def test_tyre_maps_to_discarded_tyre():
    assert keyword_fallback("Pile of old tyres in the yard") == SiteType.DISCARDED_TYRE


def test_tank_maps_to_water_tank():
    assert keyword_fallback("Water tank left uncovered") == SiteType.WATER_TANK


def test_barrel_maps_to_water_tank():
    assert keyword_fallback("Old barrel full of rainwater") == SiteType.WATER_TANK


def test_drain_maps_to_blocked_drain():
    assert keyword_fallback("Blocked drain outside the house") == SiteType.BLOCKED_DRAIN


def test_gutter_maps_to_blocked_drain():
    assert keyword_fallback("Gutter overflowing after rain") == SiteType.BLOCKED_DRAIN


def test_construction_maps_to_construction_site():
    assert (
        keyword_fallback("Water pooling at the construction next door")
        == SiteType.CONSTRUCTION_SITE
    )


def test_bottle_maps_to_open_container():
    assert keyword_fallback("Empty bottles collecting water") == SiteType.OPEN_CONTAINER


def test_bucket_maps_to_open_container():
    assert keyword_fallback("Bucket left out in the rain") == SiteType.OPEN_CONTAINER


def test_tyre_wins_over_container_when_both_present():
    assert (
        keyword_fallback("Discarded tyres and bottles behind the shop")
        == SiteType.DISCARDED_TYRE
    )


def test_unmatched_maps_to_other():
    assert keyword_fallback("Something strange near the field") == SiteType.OTHER


def test_suggest_uses_fallback_without_api_key(monkeypatch):
    monkeypatch.setattr("app.ai_suggest.GEMINI_API_KEY", "")
    site_type, source = suggest_site_type("Old barrel full of rainwater")
    assert site_type == SiteType.WATER_TANK
    assert source == "fallback"
