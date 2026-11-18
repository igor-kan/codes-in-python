from typing import Dict, List, Optional, Tuple
import heapq
import math
from models import *
from exceptions import ValidationError

def pt_sz(n: Optional[PTNode]) -> int:
    return 0 if n is None else n.sz

def pt_sum(n: Optional[PTNode]) -> int:
    return 0 if n is None else n.total

def pt_make(val: int, prio: int, l: Optional[PTNode] = None, r: Optional[PTNode] = None) -> PTNode:
    return PTNode(val, prio, 1 + pt_sz(l) + pt_sz(r), val + pt_sum(l) + pt_sum(r), l, r)

def pt_split(u: Optional[PTNode], k: int) -> Tuple[Optional[PTNode], Optional[PTNode]]:
    if u is None:
        return None, None
    lsz = pt_sz(u.l)
    if k <= lsz:
        ll, lr = pt_split(u.l, k)
        return ll, pt_make(u.val, u.prio, lr, u.r)
    rl, rr = pt_split(u.r, k - lsz - 1)
    return pt_make(u.val, u.prio, u.l, rl), rr

def pt_merge(a: Optional[PTNode], b: Optional[PTNode]) -> Optional[PTNode]:
    if a is None: return b
    if b is None: return a
    if a.prio > b.prio:
        return pt_make(a.val, a.prio, a.l, pt_merge(a.r, b))
    return pt_make(b.val, b.prio, pt_merge(a, b.l), b.r)
