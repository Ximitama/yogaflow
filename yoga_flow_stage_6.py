# === Stage 6: Связи между сущностями ===
# Project: YogaFlow
# yoga_flow/step6.py

"""YogaFlow. Этап 6: получение поз для последовательности и проверка целостности связи."""

from dataclasses import dataclass, field
from typing import Dict, List, Iterable, Optional


@dataclass
class Pose:
    """Поза в последовательности йоги."""
    name: str
    duration: int = 0
    level: str = "любой"


@dataclass
class Sequence:
    """Последовательность поз йоги."""
    name: str
    level: str
    duration: int
    focus: str
    poses: List[Pose] = field(default_factory=list)


class SequenceRepository:
    """Хранилище последовательностей с поддержкой связей к позам."""

    def __init__(self, sequences: Optional[Iterable[Sequence]] = None):
        self._sequences: Dict[str, Sequence] = {}
        for sequence in sequences or []:
            self._sequences[sequence.name] = sequence

    def add(self, sequence: Sequence) -> None:
        self._sequences[sequence.name] = sequence

    def __contains__(self, name: str) -> bool:
        return name in self._sequences

    def __iter__(self):
        return iter(self._sequences.values())


class LinkIntegrityError(Exception):
    """Исключение, возникающее при нарушении целостности связи последовательности с позами."""


def resolve_poses(sequence: Sequence) -> List[Pose]:
    """Возвращает все позы для заданной последовательности."""
    return list(sequence.poses)


def validate_links(sequence: Sequence) -> List[str]:
    """Проверяет целостность связей позы внутри последовательности.

    Возвращает список сообщений об ошибках. Пустой список означает, что
    все ссылки валидны.
    """
    errors: List[str] = []

    for pose in sequence.poses:
        if not pose.name:
            errors.append(f"Поза '{sequence.name}' содержит пустое имя позы")
        if pose.duration < 0:
            errors.append(
                f"Поза '{pose.name}' имеет отрицательную длительность"
            )

    return errors


def get_poses_for_sequence(
    repository: SequenceRepository, sequence_name: str
) -> List[Pose]:
    """Получает все позы для заданной последовательности и проверяет целостность.

    Если последовательность отсутствует в хранилище, поднимается исключение.
    Если обнаружены нарушения целостности связей, поднимается исключение.
    """
    if sequence_name not in repository:
        raise KeyError(f"Последовательность '{sequence_name}' не найдена")

    sequence = repository[sequence_name]

    errors = validate_links(sequence)
    if errors:
        raise LinkIntegrityError(
            f"Последовательность '{sequence_name}': "
            + "; ".join(errors)
        )

    return resolve_poses(sequence)
