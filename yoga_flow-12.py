# === Stage 12: Постраничный вывод ===
# Project: YogaFlow
from typing import List, Tuple


def page_size_from_length(length: int, page_size: int) -> int:
    if page_size <= 0:
        raise ValueError("page_size должен быть положительным")
    return min(page_size, length) if length else page_size


def total_pages(length: int, page_size: int) -> int:
    if page_size <= 0:
        raise ValueError("page_size должен быть положительным")
    if length <= 0:
        return 0
    return (length + page_size - 1) // page_size


def paginate_sequences(sequences: List, page: int, page_size: int) -> Tuple[List, int, int]:
    if page < 1:
        raise ValueError("page должен быть >= 1")
    total = total_pages(len(sequences), page_size)
    if page > total:
        return [], page, total
    start = (page - 1) * page_size
    return sequences[start:start + page_size], page, total


def page_controls(current_page: int, total_pages: int) -> Tuple[int, int, int]:
    prev = current_page - 1
    next_page = current_page + 1
    return prev, next_page, total_pages
