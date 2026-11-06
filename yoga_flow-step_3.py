# === Stage 3: Хранилище в памяти ===
# Project: YogaFlow
memory_store.py

from typing import Dict, List, Optional

Sequence = dict


def generate_sequence_id() -> str:
    suffix = ""
    counter = 1
    while True:
        candidate = f"seq_{counter}" + suffix
        if candidate not in _sequences:
            _sequences[candidate] = None
            return candidate
        counter += 1


_sequences: Dict[str, Optional[Sequence]] = {}


def add_sequence(name: str, level: str, duration: float, focus: str) -> str:
    sequence_id = generate_sequence_id()
    _sequences[sequence_id] = {
        "id": sequence_id,
        "name": name,
        "level": level,
        "duration": duration,
        "focus": focus,
    }
    return sequence_id


def get_sequence(sequence_id: str) -> Optional[Sequence]:
    return _sequences.get(sequence_id)


def list_sequences() -> List[Sequence]:
    return list(_sequences.values())
