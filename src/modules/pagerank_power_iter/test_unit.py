from core import SparsePageRank
from invariants import verify_stochastic_stationary


def run_tests() -> None:
    cyc = [(i, (i + 1) % 5) for i in range(5)]
    res = SparsePageRank().compute(5, cyc)
    verify_stochastic_stationary(res)
    assert all(abs(x - 0.2) < 1e-8 for x in res.ranks)

    # Dangling sink conservation test
    sink_g = [(0, 1), (0, 2), (1, 2)]
    res2 = SparsePageRank().compute(4, sink_g)
    verify_stochastic_stationary(res2)
    assert res2.ranks[2] > res2.ranks[3]


if __name__ == "__main__":
    run_tests()
