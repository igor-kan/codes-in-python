from typing import Dict, List, Optional, Tuple
import heapq
import math
from models import *
from exceptions import ValidationError

def floyd_apsp(mat: List[List[float]]) -> Tuple[bool, List[List[float]]]:
    n = len(mat)
    d = [list(row) for row in mat]
    inf = 1e15
    for k in range(n):
        for i in range(n):
            if d[i][k] >= inf:
                continue
            for j in range(n):
                if d[k][j] >= inf:
                    continue
                if d[i][k] + d[k][j] < d[i][j]:
                    d[i][j] = d[i][k] + d[k][j]
    neg = any(d[i][i] < 0.0 for i in range(n))
    return neg, d
