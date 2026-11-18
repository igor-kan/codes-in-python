from typing import Dict, List, Optional, Tuple
import heapq
import math
from models import *
from exceptions import ValidationError

def build_cartesian(arr: List[int]) -> CartTree:
    n = len(arr)
    left = [-1] * n
    right = [-1] * n
    st: List[int] = []
    for i, v in enumerate(arr):
        last = -1
        while st and arr[st[-1]] > v:
            last = st.pop()
        if st:
            right[st[-1]] = i
        if last != -1:
            left[i] = last
        st.append(i)
    return CartTree(st[0], left, right)

def query_rmq_idx(ct: CartTree, l: int, r: int) -> int:
    cur = ct.root
    while cur != -1:
        if cur < l: cur = ct.right[cur]
        elif cur > r: cur = ct.left[cur]
        else: return cur
    return -1
