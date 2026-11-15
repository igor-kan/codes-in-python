import math
from typing import Callable
from exceptions import QuadDimensionError
from models import GaussRule


class GaussLegendreEngine:
    def generate_rule(self, order: int) -> GaussRule:
        if order <= 0:
            raise QuadDimensionError("quadrature order must be positive")
        nodes = [0.0] * order
        weights = [0.0] * order
        m = (order + 1) // 2
        for i in range(m):
            z = math.cos(math.pi * (i + 0.75) / (order + 0.5))
            pp = 0.0
            for _ in range(30):
                p1, p2 = 1.0, 0.0
                for j in range(1, order + 1):
                    p3 = p2
                    p2 = p1
                    p1 = ((2.0 * j - 1.0) * z * p2 - (j - 1.0) * p3) / j
                pp = order * (z * p1 - p2) / (z * z - 1.0)
                z1 = z
                z = z1 - p1 / pp
                if abs(z - z1) < 1e-15:
                    break
            nodes[i] = -z
            nodes[order - 1 - i] = z
            w = 2.0 / ((1.0 - z * z) * pp * pp)
            weights[i] = w
            weights[order - 1 - i] = w
        return GaussRule(order=order, nodes=tuple(nodes), weights=tuple(weights))

    def integrate(self, rule: GaussRule, fn: Callable[[float], float], a: float, b: float) -> float:
        mid = 0.5 * (a + b)
        half = 0.5 * (b - a)
        return half * sum(w * fn(mid + half * x) for x, w in zip(rule.nodes, rule.weights))
