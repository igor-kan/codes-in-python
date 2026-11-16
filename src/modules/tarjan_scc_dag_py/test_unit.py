from core import IterativeTarjanSCC
from invariants import verify_scc_invariants


def run_tests() -> None:
    edges = [(0, 1), (1, 2), (2, 0), (1, 3), (3, 4), (4, 5), (5, 3)]
    res = IterativeTarjanSCC().decompose(6, edges)
    assert len(res.components) == 2
    verify_scc_invariants(6, edges, res)


if __name__ == "__main__":
    run_tests()
