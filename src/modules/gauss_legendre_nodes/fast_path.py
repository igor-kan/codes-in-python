import math
from typing import Tuple
from core import GaussLegendreEngine


def composite_gauss_integrate(fn, a: float, b: float, panels: int, order: int = 8) -> float:
    rule = GaussLegendreEngine().generate_rule(order)
    h = (b - a) / panels
    half = 0.5 * h
    acc = 0.0
    xs = rule.nodes
    ws = rule.weights
    for k in range(panels):
        mid = a + (k + 0.5) * h
        for i in range(order):
            acc += ws[i] * fn(mid + half * xs[i])
    return half * acc
