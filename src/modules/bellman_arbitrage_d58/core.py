from typing import Dict, List, Optional, Tuple
import heapq
import math
from models import *
from exceptions import ValidationError

def detect_fx_arbitrage(rates: List[List[float]]) -> bool:
    n = len(rates)
    dist = [0.0] * n
    edges: List[Tuple[int, int, float]] = []
    for i in range(n):
        for j in range(n):
            if i != j and rates[i][j] > 0.0:
                edges.append((i, j, -math.log(rates[i][j])))
    eps = 1e-9
    for _ in range(n - 1):
        for u, v, w in edges:
            if dist[u] + w < dist[v] - eps:
                dist[v] = dist[u] + w
    for u, v, w in edges:
        if dist[u] + w < dist[v] - eps:
            return True
    return False
