# === Stage 4: Редактирование записей ===
# Project: YogaFlow
from yogaflow.entities import Sequence, Pose
from yogaflow.exceptions import InvalidFieldError, NotFoundError


EDITABLE_FIELDS = {
    "name": str,
    "duration": int,
    "focus": str,
}


def update_sequence(sequence_id, updates):
    """Редактирует последовательность по идентификатору.

    Проверяет, что изменяются только допустимые поля, и что их
    значения имеют корректный тип.
    """
    if not isinstance(updates, dict):
        raise InvalidFieldError("Обновления должны быть словарём")

    allowed_keys = set(updates.keys())
    unknown = allowed_keys - set(EDITABLE_FIELDS)
    if unknown:
        raise InvalidFieldError(
            f"Недопустимые поля: {', '.join(sorted(unknown))}"
        )

    for field, value in updates.items():
        expected_type = EDITABLE_FIELDS[field]
        if not isinstance(value, expected_type):
            raise InvalidFieldError(
                f"Поле '{field}' должно быть {expected_type.__name__}"
            )

    sequence = _find_sequence(sequence_id)
    for field, value in updates.items():
        setattr(sequence, field, value)
    return sequence


def _find_sequence(sequence_id):
    sequences = _load_sequences()
    if sequence_id not in sequences:
        raise NotFoundError(f"Последовательность '{sequence_id}' не найдена")
    return sequences[sequence_id]


def _load_sequences():
    sequences = {}
    sequence_file = _get_sequences_file()
    if not sequence_file.exists():
        return sequences

    with sequence_file.open("r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            parts = line.split("|")
            if len(parts) < 4:
                continue
            try:
                sequence = Sequence(
                    id=parts[0],
                    name=parts[1],
                    level=parts[2],
                    duration=int(parts[3]),
                    focus=parts[4] if len(parts) > 4 else "",
                )
            except ValueError:
                continue
            sequences[sequence.id] = sequence
    return sequences


def _get_sequences_file():
    return _get_project_root() / "sequences.yaml"
