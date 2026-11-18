from typing import Dict, List, Optional, Tuple
import heapq
import math
from models import *
from exceptions import ValidationError

def solve_blossom_matching(n: int, edges: List[Tuple[int, int]]) -> GeneralMatching:
    g: List[List[int]] = [[] for _ in range(n)]
    for u, v in edges:
        g[u].append(v); g[v].append(u)
    match = [-1] * n
    p = [-1] * n
    base = list(range(n))
    def lca(a: int, b: int) -> int:
        used = [False] * n
        while True:
            a = base[a]; used[a] = True
            if match[a] == -1: break
            a = p[match[a]]
        while True:
            b = base[b]
            if used[b]: return b
            b = p[match[b]]
    def mark_path(v: int, b: int, child: int, blossom: List[bool]) -> None:
        while base[v] != b:
            blossom[base[v]] = blossom[base[match[v]]] = True
            p[v] = child
            child = match[v]
            v = p[match[v]]
    for root in range(n):
        if match[root] != -1: continue
        used = [False] * n
        p = [-1] * n
        base = list(range(n))
        used[root] = True
        q = [root]
        finish = -1
        for v in q:
            for to in g[v]:
                if base[v] == base[to] or match[v] == to: continue
                if to == root or (match[to] != -1 and p[match[to]] != -1):
                    cb = lca(v, to)
                    blossom = [False] * n
                    mark_path(v, cb, to, blossom)
                    mark_path(to, cb, v, blossom)
                    for i in range(n):
                        if blossom[base[i]]:
                            base[i] = cb
                            if not used[i]:
                                used[i] = True; q.append(i)
                elif p[to] == -1:
                    p[to] = v
                    if match[to] == -1:
                        finish = to; break
                    used[match[to]] = True; q.append(match[to])
            if finish != -1: break
        cur = finish
        while cur != -1:
            pv = p[cur]; nxt = match[pv]
            match[cur] = pv; match[pv] = cur
            cur = nxt
    return GeneralMatching(sum(1 for i, m in enumerate(match) if m > i), match)
