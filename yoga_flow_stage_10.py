# === Stage 10: Теги ===
# Project: YogaFlow
from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class SequenceTag:
    name: str
    color: str = "#888888"


@dataclass
class Sequence:
    name: str
    level: int
    duration: int
    focus: str
    tags: List[str] = field(default_factory=list)


class SequenceTagManager:
    def __init__(self):
        self._tags: Dict[str, SequenceTag] = {}

    def add_tag(self, name: str, color: str = "#888888") -> SequenceTag:
        if name not in self._tags:
            self._tags[name] = SequenceTag(name, color)
        return self._tags[name]

    def remove_tag(self, name: str) -> bool:
        return self._tags.pop(name, None) is not None

    def get_tag(self, name: str) -> Optional[SequenceTag]:
        return self._tags.get(name)

    def find_sequences(self, tag_name: str, sequences: List[Sequence]) -> List[Sequence]:
        tag = self.get_tag(tag_name)
        if tag is None:
            return []
        return [s for s in sequences if tag_name in s.tags]


def attach_tag(sequences: List[Sequence], tag_name: str, manager: SequenceTagManager) -> List[Sequence]:
    tag = manager.get_tag(tag_name)
    for seq in sequences:
        if tag_name not in seq.tags:
            seq.tags.append(tag_name)
    return sequences


def detach_tag(sequences: List[Sequence], tag_name: str, manager: SequenceTagManager) -> List[Sequence]:
    tag = manager.get_tag(tag_name)
    for seq in sequences:
        if tag_name in seq.tags:
            seq.tags.remove(tag_name)
    return sequences
