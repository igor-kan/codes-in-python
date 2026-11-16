import math
from typing import List, Sequence
from models import AssignmentResult
from validation import validate_cost_matrix


class HungarianPotentialSolver:
    def solve_min_cost(self, cost_matrix: Sequence[Sequence[float]]) -> AssignmentResult:
        rows, cols, swapped = validate_cost_matrix(cost_matrix)
        mat: List[List[float]] = (
            [[float(cost_matrix[c][r]) for c in range(len(cost_matrix))] for r in range(len(cost_matrix[0]))]
            if swapped
            else [[float(v) for v in row] for row in cost_matrix]
        )
        n = rows
        m = cols
        u = [0.0] * (n + 1)
        v = [0.0] * (m + 1)
        p = [0] * (m + 1)
        way = [0] * (m + 1)

        for i in range(1, n + 1):
            p[0] = i
            j0 = 0
            minv = [math.inf] * (m + 1)
            used = [False] * (m + 1)
            while True:
                used[j0] = True
                i0 = p[j0]
                delta = math.inf
                j1 = 0
                for j in range(1, m + 1):
                    if not used[j]:
                        cur = mat[i0 - 1][j - 1] - u[i0] - v[j]
                        if cur < minv[j]:
                            minv[j] = cur
                            way[j] = j0
                        if minv[j] < delta:
                            delta = minv[j]
                            j1 = j
                for j in range(m + 1):
                    if used[j]:
                        u[p[j]] += delta
                        v[j] -= delta
                    else:
                        minv[j] -= delta
                j0 = j1
                if p[j0] == 0:
                    break
            while True:
                j1 = way[j0]
                p[j0] = p[j1]
                j0 = j1
                if j0 == 0:
                    break

        ans = [-1] * n
        for j in range(1, m + 1):
            if p[j] > 0:
                ans[p[j] - 1] = j - 1

        if swapped:
            col_to_row = [-1] * len(cost_matrix)
            for c_idx, r_idx in enumerate(ans):
                col_to_row[r_idx] = c_idx
            total = sum(float(cost_matrix[r][c]) for r, c in enumerate(col_to_row) if c >= 0)
            return AssignmentResult(tuple(col_to_row), total, tuple(v[1:]), tuple(u[1:]))

        total = sum(float(cost_matrix[r][ans[r]]) for r in range(n))
        return AssignmentResult(tuple(ans), total, tuple(u[1:]), tuple(v[1:]))
