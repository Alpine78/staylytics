import pytest

from staylytics.money import parse_money_to_cents


def test_regular_euro_amount():
    assert parse_money_to_cents(12.55) == 1255


def test_regular_no_decimal_euro_amount():
    assert parse_money_to_cents(12) == 1200


def test_string_euro_amoun():
    assert parse_money_to_cents("12.55") == 1255


def test_negative_euro_amount():
    assert parse_money_to_cents(-12.55) == -1255


def test_comma_raises_value_error():
    with pytest.raises(ValueError):
        parse_money_to_cents("45,91")


def test_none_raises_error():
    with pytest.raises(ValueError):
        parse_money_to_cents(None)


def test_empty_raises_error():
    with pytest.raises(ValueError):
        parse_money_to_cents("")


def test_too_many_decimals():
    with pytest.raises(ValueError):
        parse_money_to_cents(45.123)

    with pytest.raises(ValueError):
        parse_money_to_cents("744.654")


def test_emplty_values_behavior():
    with pytest.raises(ValueError, match="Empty values are not allowed"):
        parse_money_to_cents(None)

    with pytest.raises(ValueError, match="Empty values are not allowed"):
        parse_money_to_cents("")

    assert parse_money_to_cents(None, allow_empty=True) == 0
    assert parse_money_to_cents("", allow_empty=True) == 0
