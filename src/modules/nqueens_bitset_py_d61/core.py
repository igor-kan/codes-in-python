from typing import Dict, List, Optional, Tuple
import heapq
import math
from models import *
from exceptions import ValidationError

def count_n_queens(n: int) -> int:
    if not isinstance(n, int) or n <= 0:
        raise ValidationError("n must be a positive integer")
    if n > 16:
        raise ValidationError("n must not exceed 16")
    full = (1 << n) - 1

    def solve(cols: int, diag_down: int, diag_up: int) -> int:
        if cols == full:
            return 1
        total = 0
        available = full & ~(cols | diag_down | diag_up)
        while available:
            bit = available & -available
            available ^= bit
            total += solve(cols | bit, (diag_down | bit) << 1, (diag_up | bit) >> 1)
        return total

    return solve(0, 0, 0)


def first_n_queens(n: int) -> Tuple[int, ...]:
    if not isinstance(n, int) or n <= 0:
        raise ValidationError("n must be a positive integer")
    if n > 16:
        raise ValidationError("n must not exceed 16")
    full = (1 << n) - 1
    placed: List[int] = []

    def solve(cols: int, diag_down: int, diag_up: int) -> bool:
        if cols == full:
            return True
        available = full & ~(cols | diag_down | diag_up)
        while available:
            bit = available & -available
            available ^= bit
            placed.append(bit.bit_length() - 1)
            if solve(cols | bit, (diag_down | bit) << 1, (diag_up | bit) >> 1):
                return True
            placed.pop()
        return False

    if not solve(0, 0, 0):
        return ()
    return tuple(placed)


def queens_result(n: int) -> QueensResult:
    count = count_n_queens(n)
    return QueensResult(n=n, count=count, first=first_n_queens(n))
