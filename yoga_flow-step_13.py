# === Stage 13: Быстрые фильтры ===
# Project: YogaFlow
from datetime import date, timedelta


def _get_today() -> date:
    return date.today()


def _dates_in_week(today: date) -> list[date]:
    start = today - timedelta(days=today.weekday())
    return [start + timedelta(days=i) for i in range(7)]


def filter_by_status(records, today=None) -> dict:
    if today is None:
        today = _get_today()
    week_dates = _dates_in_week(today)
    today_str = today.isoformat()
    result = {
        "today": [],
        "this_week": [],
        "overdue": [],
    }
    for record in records:
        record_date = record.get("date")
        if record_date is None:
            continue
        record_date = record_date.isoformat()
        if record_date == today_str:
            result["today"].append(record)
        elif record_date in week_dates:
            result["this_week"].append(record)
        elif record_date < today_str:
            result["overdue"].append(record)
    return result


def filter_records(records, status) -> list:
    if status == "today":
        return filter_by_status(records)["today"]
    if status == "this_week":
        return filter_by_status(records)["this_week"]
    if status == "overdue":
        return filter_by_status(records)["overdue"]
    return []
