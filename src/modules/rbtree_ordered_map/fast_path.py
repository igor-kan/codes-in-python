from typing import Optional
from core import RedBlackOrderedMap


def lower_bound(tree: RedBlackOrderedMap, target: int) -> Optional[int]:
    cur = tree.root
    ans: Optional[int] = None
    while cur is not tree.nil:
        if cur.key >= target:
            ans = cur.key
            cur = cur.left  # type: ignore[assignment]
        else:
            cur = cur.right  # type: ignore[assignment]
    return ans
