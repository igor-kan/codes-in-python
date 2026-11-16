from core import BranchAndBoundKnapsack
from invariants import verify_knapsack_plan
from models import KnapsackItem


def run_tests() -> None:
    items = [
        KnapsackItem(0, 10, 60),
        KnapsackItem(1, 20, 100),
        KnapsackItem(2, 30, 120),
    ]
    plan = BranchAndBoundKnapsack().solve(items, 50)
    assert plan.optimal_value == 220
    assert plan.selected_ids == (1, 2)
    verify_knapsack_plan(items, 50, plan)


if __name__ == "__main__":
    run_tests()
