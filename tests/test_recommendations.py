from app.services.recommendation_service import categorize, LOW_THRESHOLD, HIGH_THRESHOLD


def test_categorize_high_value():
    category, _, _ = categorize(HIGH_THRESHOLD + 1)
    assert category == "high"


def test_categorize_low_value():
    category, _, _ = categorize(LOW_THRESHOLD - 1)
    assert category == "low"


def test_categorize_moderate_value():
    midpoint = (LOW_THRESHOLD + HIGH_THRESHOLD) / 2
    category, _, _ = categorize(midpoint)
    assert category == "moderate"


def test_categorize_returns_reason_with_actual_thresholds():
    _, _, reason = categorize(HIGH_THRESHOLD + 1)
    assert f"{HIGH_THRESHOLD:.2f}" in reason
    