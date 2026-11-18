from typing import Dict, List, Optional, Tuple
import heapq
import math
from models import *
from exceptions import ValidationError

def aho_corasick_count(patterns: List[str], text: str) -> AcSummary:
    nxt: List[Dict[str, int]] = [{}]
    fail: List[int] = [0]
    out: List[int] = [0]
    for pat in patterns:
        u = 0
        for ch in pat:
            if ch not in nxt[u]:
                nxt[u][ch] = len(nxt)
                nxt.append({})
                fail.append(0)
                out.append(0)
            u = nxt[u][ch]
        out[u] += 1
    q = list(nxt[0].values())
    for u in q:
        for ch, v in nxt[u].items():
            q.append(v)
            f = fail[u]
            while f > 0 and ch not in nxt[f]:
                f = fail[f]
            fail[v] = nxt[f].get(ch, 0)
            out[v] += out[fail[v]]
    u = 0
    hits = 0
    for ch in text:
        while u > 0 and ch not in nxt[u]:
            u = fail[u]
        u = nxt[u].get(ch, 0)
        hits += out[u]
    return AcSummary(hits=hits, states=len(nxt))
