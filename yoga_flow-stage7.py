# === Stage 7: Генерация идентификаторов ===
# Project: YogaFlow
from __future__ import annotations

PREFIX = "yoga"


class IDCollisionError(Exception):
    """Исключение при попытке создать дублирующийся идентификатор."""

    def __init__(self, identifier: str, existing: str) -> None:
        self.identifier = identifier
        self.existing = existing
        super().__init__(
            f"ID {identifier!r} уже существует, коллизия с {existing!r}"
        )


def generate_unique_id(
    namespace: str,
    values: list[str],
    counter: int = 1,
    max_attempts: int = 1000,
) -> str:
    """Генерирует уникальный идентификатор вида <префикс>-<пространство>-<значение>-<индекс>.

    Аргументы:
        namespace: пространство имен для изоляции префиксов.
        values: список уже занятых значений (для проверки коллизий).
        counter: счётчик для формирования уникального суффикса.
        max_attempts: максимальное число попыток генерации.

    Возвращает строку с уникальным идентификатором.

    Поднимаем IDCollisionError, если не удалось сгенерировать уникальный ID.
    """
    if counter > max_attempts:
        raise IDCollisionError(namespace, "max_attempts exceeded")

    candidate = f"{PREFIX}-{namespace}-{counter}"
    if candidate in values:
        counter += 1
        return generate_unique_id(namespace, values, counter, max_attempts)

    values.append(candidate)
    return candidate


def is_valid_id(identifier: str) -> bool:
    """Проверяет, что идентификатор соответствует формату проекта."""
    if not isinstance(identifier, str):
        return False
    if not identifier.startswith(f"{PREFIX}-"):
        return False
    return identifier.count("-") >= 2


def build_id(values: list[str], namespace: str, counter: int = 1) -> str:
    """Удобная обёртка для генерации ID с проверкой коллизий."""
    return generate_unique_id(namespace, values, counter)
