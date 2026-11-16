from typing import Sequence
from exceptions import KnapsackDomainError
from fast_path import dp_oracle_value
from models import KnapsackItem, KnapsackPlan


def verify_knapsack_plan(items: Sequence[KnapsackItem], capacity: int, plan: KnapsackPlan) -> None:
    by_id = {it.item_id: it for it in items}
    wt = sum(by_id[i].weight for i in plan.selected_ids)
    val = sum(by_id[i].value for i in plan.selected_ids)
    if wt > capacity or wt != plan.total_weight or val != plan.optimal_value:
        raise KnapsackDomainError("knapsack weight or value accounting invariant broken")
    oracle = dp_oracle_value(items, capacity)
    if val != oracle:
        raise KnapsackDomainError(f"suboptimal value {val} != DP oracle {oracle}")
