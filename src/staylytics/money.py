from decimal import ROUND_HALF_UP, Decimal


def parse_money_to_cents(euro_amount, allow_empty=False):
    # 1. Käsitellään tyhjät syötteet (None tai tyhjä merkkijono)
    if euro_amount is None or (isinstance(euro_amount, str) and euro_amount.strip() == ""):
        if allow_empty:
            return 0
        raise ValueError("Empty values are not allowed unless explicitly requested")

    # 2. Hylätään pilkulliset desimaalit
    if isinstance(euro_amount, str) and "," in euro_amount:
        raise ValueError("Reject comma decimal values")

    amount_str = str(euro_amount)

    # 3. Tarkistetaan desimaalien määrä
    if "." in amount_str:
        parts = amount_str.split(".")
        if len(parts[1]) > 2:
            raise ValueError("Reject values with more than two decimal places")

    # 4. Tehdään turvallinen laskenta
    cents = Decimal(amount_str) * 100

    return int(cents.quantize(Decimal("1"), rounding=ROUND_HALF_UP))
