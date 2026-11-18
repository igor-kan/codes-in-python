from typing import Dict, List, Optional, Tuple
import heapq
import math
from models import *
from exceptions import ValidationError

def build_alias_table(weights: List[float]) -> AliasTable:
    n = len(weights)
    tot = sum(weights)
    scaled = [w * n / tot for w in weights]
    prob = [1.0] * n
    alias = list(range(n))
    small = [i for i, v in enumerate(scaled) if v < 1.0]
    large = [i for i, v in enumerate(scaled) if v >= 1.0]
    while small and large:
        s = small.pop()
        l = large.pop()
        prob[s] = scaled[s]
        alias[s] = l
        scaled[l] = (scaled[l] + scaled[s]) - 1.0
        if scaled[l] < 1.0:
            small.append(l)
        else:
            large.append(l)
    return AliasTable(prob, alias)

def sample_alias(tbl: AliasTable, bucket: int, u01: float) -> int:
    return bucket if u01 < tbl.prob[bucket] else tbl.alias[bucket]
