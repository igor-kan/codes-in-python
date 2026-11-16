import random
from concurrency import batch_pagerank
from invariants import verify_stochastic_stationary


def run_properties() -> None:
    rng = random.Random(42)
    tasks = [(16, [(rng.randrange(16), rng.randrange(16)) for _ in range(40)]) for _ in range(6)]
    for res in batch_pagerank(tasks):
        verify_stochastic_stationary(res)


if __name__ == "__main__":
    run_properties()
