# === Stage 2: Проверка полей ===
# Project: YogaFlow
import re


def normalize_text(value):
    if value is None:
        return ""
    return re.sub(r"\s+", " ", str(value)).strip()


def normalize_level(value):
    if value is None:
        return ""
    text = str(value).strip().lower()
    if text in ("начинающий", "новичок", "beginner", "easy"):
        return "beginner"
    if text in ("средний", "средне", "intermediate", "medium"):
        return "intermediate"
    if text in ("продвинутый", "продвинут", "advanced", "hard"):
        return "advanced"
    return text


def normalize_duration(value):
    if value is None:
        return None
    text = str(value).strip()
    match = re.match(r"^(\d+)([сминут]?|минут?)$", text)
    if not match:
        return None
    number = int(match.group(1))
    if number <= 0:
        return None
    return number


def validate_sequence(name, level, duration, focus):
    errors = []

    if not name or not name.strip():
        errors.append("Название последовательности не может быть пустым.")
    name = normalize_text(name)

    level = normalize_level(level)
    if not level:
        errors.append("Уровень последовательности не может быть пустым.")

    duration = normalize_duration(duration)
    if duration is None:
        errors.append("Длительность должна быть положительным числом минут.")

    if not focus or not focus.strip():
        errors.append("Фокус последовательности не может быть пустым.")
    focus = normalize_text(focus)

    return name, level, duration, focus, errors
