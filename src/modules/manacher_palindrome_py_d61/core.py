from typing import Dict, List, Optional, Tuple
import heapq
import math
from models import *
from exceptions import ValidationError

def _odd_radii(text: str) -> List[int]:
    n = len(text)
    d = [0] * n
    left, right = 0, -1
    for i in range(n):
        k = 1 if i > right else min(d[left + right - i], right - i + 1)
        while i - k >= 0 and i + k < n and text[i - k] == text[i + k]:
            k += 1
        d[i] = k
        if i + k - 1 > right:
            left = i - k + 1
            right = i + k - 1
    return d


def _even_radii(text: str) -> List[int]:
    n = len(text)
    d = [0] * n
    left, right = 0, -1
    for i in range(n):
        k = 0 if i > right else min(d[left + right - i + 1], right - i + 1)
        while i - k - 1 >= 0 and i + k < n and text[i - k - 1] == text[i + k]:
            k += 1
        d[i] = k
        if i + k - 1 > right:
            left = i - k
            right = i + k - 1
    return d


def longest_palindrome(text: str) -> PalindromeSpan:
    if not isinstance(text, str):
        raise ValidationError("text must be a string")
    best = PalindromeSpan(0, 0)
    for i, radius in enumerate(_odd_radii(text)):
        length = 2 * radius - 1
        start = i - radius + 1
        if length > best.length or (length == best.length and start < best.start):
            best = PalindromeSpan(start, length)
    for i, radius in enumerate(_even_radii(text)):
        length = 2 * radius
        start = i - radius
        if length > best.length or (length == best.length and start < best.start):
            best = PalindromeSpan(start, length)
    return best
