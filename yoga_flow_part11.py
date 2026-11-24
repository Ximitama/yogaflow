# === Stage 11: Группировка ===
# Project: YogaFlow
from collections import Counter


def group_by_level(sequences):
    grouped = Counter()
    for sequence in sequences:
        grouped[sequence.level] += 1
    return dict(grouped)


def group_by_level_sorted(sequences):
    grouped = Counter()
    for sequence in sequences:
        grouped[sequence.level] += 1
    return dict(sorted(grouped.items()))


def summarize_levels(sequences):
    grouped = group_by_level(sequences)
    summary = []
    for level, count in grouped.items():
        summary.append((level, count))
    return summary


if __name__ == "__main__":
    sample_sequences = [
        {"name": "Sun Salutation", "level": "beginner", "duration": 15, "focus": "warm-up"},
        {"name": "Standing Series", "level": "beginner", "duration": 20, "focus": "balance"},
        {"name": "Chair Yoga", "level": "beginner", "duration": 10, "focus": "gentle"},
        {"name": "Vinyasa Flow", "level": "intermediate", "duration": 30, "focus": "strength"},
        {"name": "Power Flow", "level": "intermediate", "duration": 40, "focus": "strength"},
        {"name": "Advanced Standing", "level": "advanced", "duration": 45, "focus": "flexibility"},
    ]

    result = group_by_level_sorted(sample_sequences)
    for level, count in result.items():
        print(f"Level: {level}, Count: {count}")
