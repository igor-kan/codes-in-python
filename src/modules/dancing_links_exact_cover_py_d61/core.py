from typing import Dict, List, Optional, Tuple
import heapq
import math
from models import *
from exceptions import ValidationError

class _DlxNode:
    __slots__ = ("left", "right", "up", "down", "col", "row", "size")

    def __init__(self, row: int = -1) -> None:
        self.left = self
        self.right = self
        self.up = self
        self.down = self
        self.col = self
        self.row = row
        self.size = 0


def _dlx_build(rows: List[List[int]], ncols: int) -> _DlxNode:
    root = _DlxNode()
    headers: List[_DlxNode] = []
    for _ in range(ncols):
        header = _DlxNode()
        header.col = header
        header.left = root.left
        header.right = root
        root.left.right = header
        root.left = header
        headers.append(header)
    for row_index, cols in enumerate(rows):
        if not cols:
            continue
        first: Optional[_DlxNode] = None
        for column in cols:
            node = _DlxNode(row_index)
            header = headers[column]
            node.col = header
            header.size += 1
            node.up = header.up
            node.down = header
            header.up.down = node
            header.up = node
            if first is None:
                first = node
            else:
                node.left = first.left
                node.right = first
                first.left.right = node
                first.left = node
    return root


def _dlx_cover(column: _DlxNode) -> None:
    column.right.left = column.left
    column.left.right = column.right
    row = column.down
    while row is not column:
        node = row.right
        while node is not row:
            node.down.up = node.up
            node.up.down = node.down
            node.col.size -= 1
            node = node.right
        row = row.down


def _dlx_uncover(column: _DlxNode) -> None:
    row = column.up
    while row is not column:
        node = row.left
        while node is not row:
            node.col.size += 1
            node.down.up = node
            node.up.down = node
            node = node.left
        row = row.up
    column.right.left = column
    column.left.right = column


def _dlx_search(root: _DlxNode, chosen: List[int], out: List[Tuple[int, ...]], limit: int) -> None:
    if len(out) >= limit:
        return
    if root.right is root:
        out.append(tuple(chosen))
        return
    column = root.right
    best = column
    while column is not root:
        if column.size < best.size:
            best = column
        column = column.right
    if best.size == 0:
        return
    _dlx_cover(best)
    row = best.down
    while row is not best:
        chosen.append(row.row)
        node = row.right
        while node is not row:
            _dlx_cover(node.col)
            node = node.right
        _dlx_search(root, chosen, out, limit)
        node = row.left
        while node is not row:
            _dlx_uncover(node.col)
            node = node.left
        chosen.pop()
        if len(out) >= limit:
            break
        row = row.down
    _dlx_uncover(best)


def exact_cover(rows: List[List[int]], ncols: int, limit: int = 1) -> ExactCoverResult:
    if not isinstance(ncols, int) or ncols <= 0:
        raise ValidationError("ncols must be a positive integer")
    if not isinstance(limit, int) or limit <= 0:
        raise ValidationError("limit must be a positive integer")
    normalized: List[List[int]] = []
    for row in rows:
        seen = set()
        for column in row:
            if not isinstance(column, int) or column < 0 or column >= ncols:
                raise ValidationError("column index must lie inside [0, ncols)")
            if column in seen:
                raise ValidationError("a row may not reference a column twice")
            seen.add(column)
        normalized.append(sorted(seen))
    root = _dlx_build(normalized, ncols)
    solutions: List[Tuple[int, ...]] = []
    _dlx_search(root, [], solutions, limit)
    return ExactCoverResult(solutions=tuple(solutions), columns=ncols)
