import random
from concurrency import batch_scc
from core import IterativeTarjanSCC
from invariants import verify_scc_invariants


def run_properties() -> None:
    # Deep 3500-vertex linear chain (would trigger RecursionError in naive recursive Tarjan)
    deep_edges = [(i, i + 1) for i in range(3500)]
    deep_res = IterativeTarjanSCC().decompose(3501, deep_edges)
    assert len(deep_res.components) == 3501

    rng = random.Random(314)
    graphs = [(14, [(rng.randrange(14), rng.randrange(14)) for _ in range(28)]) for _ in range(8)]
    for (n, es), r in zip(graphs, batch_scc(graphs)):
        verify_scc_invariants(n, es, r)


if __name__ == "__main__":
    run_properties()
