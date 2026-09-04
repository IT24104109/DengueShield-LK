from app.risk import compute_risk_level


def test_zero_is_low():
    assert compute_risk_level(0) == "Low"


def test_one_is_low():
    assert compute_risk_level(1) == "Low"


def test_two_is_medium():
    assert compute_risk_level(2) == "Medium"


def test_four_is_medium():
    assert compute_risk_level(4) == "Medium"


def test_five_is_high():
    assert compute_risk_level(5) == "High"


def test_ten_is_high():
    assert compute_risk_level(10) == "High"
