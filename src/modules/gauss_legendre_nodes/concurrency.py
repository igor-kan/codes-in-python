from concurrent.futures import ThreadPoolExecutor
from typing import Callable, List, Sequence, Tuple
from core import GaussLegendreEngine


def parallel_integrate_intervals(
    fn: Callable[[float], float], intervals: Sequence[Tuple[float, float]], order: int = 12
) -> List[float]:
    engine = GaussLegendreEngine()
    rule = engine.generate_rule(order)
    with ThreadPoolExecutor(max_workers=2) as pool:
        return list(pool.map(lambda ab: engine.integrate(rule, fn, ab[0], ab[1]), intervals))
