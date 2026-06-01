from datetime import datetime

FINNISH_MONTHS = {
    "tammik.": "01",
    "helmik.": "02",
    "maalisik.": "03",
    "huhtik.": "04",
    "toukok.": "05",
    "kesäk.": "06",
    "kesÃ¤k.": "06",
    "heinäk.": "07",
    "heinÃ¤k.": "07",
    "elok.": "08",
    "syysk.": "09",
    "lokak.": "10",
    "marrask.": "11",
    "jouluk.": "12",
}


def parse_dates(date_str):
    date_str = str(date_str).strip()

    # Finnish Booking.com dates
    for fin_month, month_num in FINNISH_MONTHS.items():
        if fin_month in date_str:
            cleaned = date_str.replace(fin_month, month_num).replace(".", "")
            try:
                dt = datetime.strptime(cleaned, "%d %m %Y")
                return dt.strftime("%Y-%m-%d")
            except ValueError:
                pass

    # English Booking.com dates
    try:
        testi = date_str.replace(",", "")
        dt = datetime.strptime(testi, "%b %d %Y")
        return dt.strftime("%Y-%m-%d")
    except ValueError:
        pass

    # Airbnb dates
    if "/" in date_str:
        parts = date_str.split("/")
        if len(parts) == 3:
            try:
                dt = datetime.strptime(date_str, "%m/%d/%Y")
                return dt.strftime("%Y-%m-%d")
            except ValueError:
                pass

    raise ValueError(f"Unknown or ambiguous date format: {date_str}")
