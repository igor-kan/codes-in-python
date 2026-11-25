from typing import Dict, List, Optional, Tuple
import heapq
import math
from models import *
from exceptions import ValidationError

def solve_lp_std(a: List[List[float]], b: List[float], c: List[float]) -> LpSolution:
    m, n = len(a), len(c)
    if m == 0 or n == 0 or any(bi < 0 for bi in b):
        raise ValidationError("standard form requires non-negative RHS b")
    width = n + m + 1
    tab = [[0.0] * width for _ in range(m + 1)]
    for i in range(m):
        for j in range(n):
            tab[i][j] = float(a[i][j])
        tab[i][n + i] = 1.0
        tab[i][-1] = float(b[i])
    for j in range(n):
        tab[m][j] = -float(c[j])
    basis = [n + i for i in range(m)]
    for _ in range(256):
        col = -1
        best_rc = -1e-9
        for j in range(n + m):
            if tab[m][j] < best_rc:
                best_rc = tab[m][j]
                col = j
        if col == -1:
            break
        row, min_ratio = -1, float("inf")
        for i in range(m):
            if tab[i][col] > 1e-9:
                ratio = tab[i][-1] / tab[i][col]
                if ratio < min_ratio - 1e-12:
                    min_ratio = ratio
                    row = i
        if row == -1:
            raise ValidationError("linear program is unbounded")
        piv = tab[row][col]
        for j in range(width):
            tab[row][j] /= piv
        for i in range(m + 1):
            if i != row and abs(tab[i][col]) > 1e-12:
                f = tab[i][col]
                for j in range(width):
                    tab[i][j] -= f * tab[row][j]
        basis[row] = col
    primal = [0.0] * n
    for i, var in enumerate(basis):
        if var < n:
            primal[var] = tab[i][-1]
    return LpSolution(objective=tab[m][-1], primal=tuple(primal))
