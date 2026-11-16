import heapq
from typing import List, Sequence, Tuple
from models import KnapsackItem, KnapsackPlan
from validation import validate_knapsack_input


def _fractional_bound(
    sorted_items: Sequence[KnapsackItem],
    capacity: int,
    idx: int,
    cur_weight: int,
    cur_value: int,
) -> float:
    if cur_weight >= capacity:
        return float(cur_value)
    bound = float(cur_value)
    w = cur_weight
    n = len(sorted_items)
    while idx < n and w + sorted_items[idx].weight <= capacity:
        w += sorted_items[idx].weight
        bound += sorted_items[idx].value
        idx += 1
    if idx < n and sorted_items[idx].weight > 0:
        bound += (capacity - w) * (sorted_items[idx].value / sorted_items[idx].weight)
    return bound


class BranchAndBoundKnapsack:
    def solve(self, items: Sequence[KnapsackItem], capacity: int) -> KnapsackPlan:
        validate_knapsack_input(items, capacity)
        if not items or capacity == 0:
            return KnapsackPlan(0, 0, (), 1)

        ordered: List[KnapsackItem] = sorted(
            items,
            key=lambda it: (it.value / it.weight if it.weight > 0 else float("inf")),
            reverse=True,
        )
        n = len(ordered)
        best_val = 0
        best_wt = 0
        best_taken: Tuple[int, ...] = ()
        explored = 0

        root_ub = _fractional_bound(ordered, capacity, 0, 0, 0)
        # Max-heap via (-upper_bound, level, weight, value, chosen_mask_tuple)
        pq: List[Tuple[float, int, int, int, Tuple[int, ...]]] = [(-root_ub, 0, 0, 0, ())]
        while pq:
            neg_ub, lvl, w, v, chosen = heapq.heappop(pq)
            explored += 1
            if -neg_ub <= best_val:
                continue
            if lvl == n:
                continue
            item = ordered[lvl]
            # Branch 1: include item if weight fits
            nw = w + item.weight
            if nw <= capacity:
                nv = v + item.value
                n_chosen = chosen + (item.item_id,)
                if nv > best_val:
                    best_val = nv
                    best_wt = nw
                    best_taken = n_chosen
                ub_inc = _fractional_bound(ordered, capacity, lvl + 1, nw, nv)
                if ub_inc > best_val:
                    heapq.heappush(pq, (-ub_inc, lvl + 1, nw, nv, n_chosen))
            # Branch 2: exclude item
            ub_exc = _fractional_bound(ordered, capacity, lvl + 1, w, v)
            if ub_exc > best_val:
                heapq.heappush(pq, (-ub_exc, lvl + 1, w, v, chosen))

        return KnapsackPlan(
            optimal_value=best_val,
            total_weight=best_wt,
            selected_ids=tuple(sorted(best_taken)),
            explored_nodes=explored,
        )
