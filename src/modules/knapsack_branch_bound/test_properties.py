import random
from concurrency import parallel_solve_instances
from invariants import verify_knapsack_plan
from models import KnapsackItem


def run_properties() -> None:
    rng = random.Random(2026)
    instances = []
    for _ in range(12):
        items = [KnapsackItem(i, rng.randint(1, 25), rng.randint(5, 80)) for i in range(14)]
        cap = rng.randint(25, 110)
        instances.append((items, cap))
    plans = parallel_solve_instances(instances)
    for (items, cap), plan in zip(instances, plans):
        verify_knapsack_plan(items, cap, plan)


if __name__ == "__main__":
    run_properties()
