from staylytics.dates import parse_dates


def test_parse_finnish_booking_date():
    assert parse_dates("25. huhtik. 2025") == "2025-04-25"


def test_parse_finnish_booking_date_weird():
    assert parse_dates("7. heinÃ¤k. 2025") == "2025-07-07"


def test_parse_english_booking_date():
    assert parse_dates("Feb 16, 2025") == "2025-02-16"


def test_parse_airbnb_date():
    assert parse_dates("05/18/2026") == "2026-05-18"
