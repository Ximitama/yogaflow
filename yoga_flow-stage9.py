# === Stage 9: Поиск по нескольким словам ===
# Project: YogaFlow
def find_sequences(sequences, *query_terms):
    query_terms = [t.strip().lower() for t in query_terms if t.strip()]
    exclusions = [t.lstrip('-').strip().lower() for t in query_terms if t.lstrip('-').startswith('-')]
    if exclusions:
        exclusions = set(exclusions)
    tokens = set(t for t in query_terms if not t.startswith('-'))
    if not query_terms:
        return list(sequences)
    result = []
    for seq in sequences:
        text = ' '.join(
            [seq.get('name', '').lower(),
             seq.get('level', '').lower(),
             seq.get('duration', '').lower(),
             seq.get('focus', '').lower()]
        )
        if any(ex in text for ex in exclusions):
            continue
        if not any(t in text for t in tokens):
            continue
        result.append(seq)
    return result


if __name__ == '__main__':
    demo = [
        {'name': 'Morning Sun Salutation', 'level': 'beginner', 'duration': 15, 'focus': 'energy'},
        {'name': 'Deep Relaxation', 'level': 'intermediate', 'duration': 30, 'focus': 'calm'},
        {'name': 'Hip Opener Flow', 'level': 'advanced', 'duration': 20, 'focus': 'flexibility'},
    ]
    print(find_sequences(demo, 'beginner', '-relax'))
    print(find_sequences(demo, 'flexibility', 'advanced'))
    print(find_sequences(demo))
