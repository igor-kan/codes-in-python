from typing import List, Optional, Tuple
from models import BLACK, RED, RbNode


class RedBlackOrderedMap:
    def __init__(self) -> None:
        self.nil = RbNode(key=0, value=0, color=BLACK)
        self.root = self.nil
        self.count = 0

    def _left_rotate(self, x: RbNode) -> None:
        y = x.right
        assert y is not None
        x.right = y.left
        if y.left is not self.nil:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is self.nil:
            self.root = y
        elif x is x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def _right_rotate(self, y: RbNode) -> None:
        x = y.left
        assert x is not None
        y.left = x.right
        if x.right is not self.nil:
            x.right.parent = y
        x.parent = y.parent
        if y.parent is self.nil:
            self.root = x
        elif y is y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x
        x.right = y
        y.parent = x

    def insert(self, key: int, value: int) -> None:
        y = self.nil
        x = self.root
        while x is not self.nil:
            y = x
            if key < x.key:
                x = x.left  # type: ignore[assignment]
            elif key > x.key:
                x = x.right  # type: ignore[assignment]
            else:
                x.value = value
                return
        z = RbNode(key=key, value=value, color=RED, left=self.nil, right=self.nil, parent=y)
        if y is self.nil:
            self.root = z
        elif key < y.key:
            y.left = z
        else:
            y.right = z
        self.count += 1
        self._fix_insert(z)

    def _fix_insert(self, z: RbNode) -> None:
        while z.parent is not None and z.parent.color == RED:
            gp = z.parent.parent
            assert gp is not None
            if z.parent is gp.left:
                u = gp.right
                assert u is not None
                if u.color == RED:
                    z.parent.color = BLACK
                    u.color = BLACK
                    gp.color = RED
                    z = gp
                else:
                    if z is z.parent.right:
                        z = z.parent
                        self._left_rotate(z)
                        gp = z.parent.parent  # type: ignore[assignment]
                    z.parent.color = BLACK
                    gp.color = RED
                    self._right_rotate(gp)
            else:
                u = gp.left
                assert u is not None
                if u.color == RED:
                    z.parent.color = BLACK
                    u.color = BLACK
                    gp.color = RED
                    z = gp
                else:
                    if z is z.parent.left:
                        z = z.parent
                        self._right_rotate(z)
                        gp = z.parent.parent  # type: ignore[assignment]
                    z.parent.color = BLACK
                    gp.color = RED
                    self._left_rotate(gp)
        self.root.color = BLACK

    def get(self, key: int) -> Optional[int]:
        x = self.root
        while x is not self.nil:
            if key < x.key:
                x = x.left  # type: ignore[assignment]
            elif key > x.key:
                x = x.right  # type: ignore[assignment]
            else:
                return x.value
        return None

    def inorder_items(self) -> List[Tuple[int, int]]:
        out: List[Tuple[int, int]] = []
        stack: List[RbNode] = []
        cur = self.root
        while stack or cur is not self.nil:
            while cur is not self.nil:
                stack.append(cur)
                cur = cur.left  # type: ignore[assignment]
            cur = stack.pop()
            out.append((cur.key, cur.value))
            cur = cur.right  # type: ignore[assignment]
        return out
