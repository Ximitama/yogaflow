# === Stage 5: Удаление и восстановление ===
# Project: YogaFlow
import uuid
from datetime import datetime


class Sequence:
    def __init__(self, name, level, duration, focus, poses=None):
        self.id = str(uuid.uuid4())
        self.name = name
        self.level = level
        self.duration = duration
        self.focus = focus
        self.poses = poses or []
        self.deleted = False
        self.deleted_at = None
        self.deleted_reason = None

    @property
    def is_deleted(self):
        return self.deleted

    def delete(self, reason="Пользователь удалил последовательность"):
        self.deleted = True
        self.deleted_at = datetime.now().isoformat()
        self.deleted_reason = reason

    def restore(self):
        self.deleted = False
        self.deleted_at = None
        self.deleted_reason = None


def find_sequence_by_id(sequences, sequence_id):
    for sequence in sequences:
        if not sequence.is_deleted and sequence.id == sequence_id:
            return sequence
    return None


def find_deleted_sequence_by_id(sequences, sequence_id):
    for sequence in sequences:
        if sequence.is_deleted and sequence.id == sequence_id:
            return sequence
    return None


def remove_sequence(sequences, sequence_id):
    sequence = find_sequence_by_id(sequences, sequence_id)
    if sequence is None:
        return False
    sequence.delete()
    return True


def restore_sequence(sequences, sequence_id):
    sequence = find_deleted_sequence_by_id(sequences, sequence_id)
    if sequence is None:
        return False
    sequence.restore()
    return True


def get_active_sequences(sequences):
    return [s for s in sequences if not s.is_deleted]


def get_deleted_sequences(sequences):
    return [s for s in sequences if s.is_deleted]
