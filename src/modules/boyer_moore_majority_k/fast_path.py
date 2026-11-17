from typing import List, Optional

def boyer_moore_single_majority(arr: List[int]) -> Optional[int]:
    cand, cnt = None, 0
    for x in arr:
        if cnt == 0:
            cand, cnt = x, 1
        elif cand == x:
            cnt += 1
        else:
            cnt -= 1
    return cand if cand is not None and arr.count(cand) > len(arr) // 2 else None
