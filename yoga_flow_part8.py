# === Stage 8: Сортировка записей ===
# Project: YogaFlow
import functools


def sort_sequences_by_name(records, ascending=True):
    """Сортирует последовательности по названию."""
    if records is None:
        return records
    key = lambda item: item.get("name") or ""
    return sorted(records, key=key, reverse=not ascending)


def sort_sequences_by_created_at(records, ascending=True):
    """Сортирует последовательности по дате создания."""
    if records is None:
        return records
    key = lambda item: item.get("created_at") or 0
    return sorted(records, key=key, reverse=not ascending)


def sort_sequences(records, field="name", ascending=True):
    """
    Универсальная сортировка записей последовательности.

    Параметры:
        records: список словарей или None.
        field: имя поля для сортировки (по умолчанию "name").
        ascending: True — возрастание, False — убывание.

    Возвращает новый список, не изменяя входной.
    """
    if not records:
        return records

    @functools.cmp_to_key
    def compare(a, b):
        a_value = a.get(field)
        b_value = b.get(field)
        if a_value == b_value:
            return 0
        try:
            if isinstance(a_value, (int, float)) and isinstance(
                b_value, (int, float)
            ):
                return (a_value > b_value) - (a_value < b_value)
        except TypeError:
            pass
        a_str = "" if a_value is None else str(a_value)
        b_str = "" if b_value is None else str(b_value)
        return (a_str > b_str) - (a_str < b_str)

    return sorted(records, key=compare, reverse=not ascending)
