from core import RedBlackOrderedMap
from models import BLACK, RED, RbNode


def verify_rbtree(tree: RedBlackOrderedMap) -> None:
    assert tree.root.color == BLACK

    def check(node: RbNode) -> int:
        if node is tree.nil:
            return 1
        assert node.left is not None and node.right is not None
        if node.color == RED:
            assert node.left.color == BLACK and node.right.color == BLACK
        if node.left is not tree.nil:
            assert node.left.key < node.key
        if node.right is not tree.nil:
            assert node.right.key > node.key
        lh = check(node.left)
        rh = check(node.right)
        assert lh == rh
        return lh + (1 if node.color == BLACK else 0)

    check(tree.root)
