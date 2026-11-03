# === Stage 1: Каркас модуля ===
# Project: YogaFlow
from dataclasses import dataclass, field
from typing import List


@dataclass
class Sequence:
    name: str
    level: str
    duration: int
    focus: str


def make_demo_sequences() -> List[Sequence]:
    return [
        Sequence(name="Солнечное приветствие", level="начальный", duration=15, focus="энергия"),
        Sequence(name="Спокойствие и дыхание", level="средний", duration=20, focus="расслабление"),
        Sequence(name="Укрепление тела", level="продвинутый", duration=30, focus="сила"),
    ]


def main() -> None:
    for seq in make_demo_sequences():
        print(f"Последовательность: {seq.name}")
        print(f"Уровень: {seq.level}")
        print(f"Длительность: {seq.duration} минут")
        print(f"Фокус: {seq.focus}")
        print("-" * 40)


if __name__ == "__main__":
    main()
