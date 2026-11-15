from typing import List
from exceptions import SimplexDomainError
from models import LinearProgram, SimplexSolution


class BlandSimplexSolver:
    def maximize(self, lp: LinearProgram, max_pivots: int = 5000) -> SimplexSolution:
        m = len(lp.a_rows)
        n = len(lp.c)
        cols = n + m
        tab: List[List[float]] = [[0.0] * (cols + 1) for _ in range(m + 1)]
        for i in range(m):
            if lp.b[i] < 0.0:
                raise SimplexDomainError("phase-2 simplex requires feasible origin b >= 0")
            for j in range(n):
                tab[i][j] = lp.a_rows[i][j]
            tab[i][n + i] = 1.0
            tab[i][cols] = lp.b[i]
        for j in range(n):
            tab[m][j] = -lp.c[j]
        basis = [n + i for i in range(m)]

        pivots = 0
        while pivots < max_pivots:
            entering = -1
            for j in range(cols):
                if tab[m][j] < -1e-10:
                    entering = j
                    break
            if entering == -1:
                x = [0.0] * n
                for i, bcol in enumerate(basis):
                    if bcol < n:
                        x[bcol] = tab[i][cols]
                return SimplexSolution("OPTIMAL", tab[m][cols], tuple(x), pivots)

            leaving = -1
            best_ratio = float("inf")
            for i in range(m):
                a_ie = tab[i][entering]
                if a_ie > 1e-10:
                    ratio = tab[i][cols] / a_ie
                    if ratio < best_ratio - 1e-12 or (abs(ratio - best_ratio) <= 1e-12 and basis[i] < basis[leaving]):
                        best_ratio = ratio
                        leaving = i
            if leaving == -1:
                return SimplexSolution("UNBOUNDED", float("inf"), tuple([0.0] * n), pivots)

            piv_val = tab[leaving][entering]
            inv_piv = 1.0 / piv_val
            for j in range(cols + 1):
                tab[leaving][j] *= inv_piv
            for i in range(m + 1):
                if i == leaving or abs(tab[i][entering]) < 1e-15:
                    continue
                factor = tab[i][entering]
                row_i = tab[i]
                row_l = tab[leaving]
                for j in range(cols + 1):
                    row_i[j] -= factor * row_l[j]
            basis[leaving] = entering
            pivots += 1

        raise SimplexDomainError("simplex exceeded max_pivots")
