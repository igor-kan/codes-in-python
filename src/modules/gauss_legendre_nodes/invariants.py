import math
from models import GaussRule


def verify_rule_invariants(rule: GaussRule) -> None:
    n = rule.order
    assert len(rule.nodes) == n and len(rule.weights) == n
    assert math.isclose(sum(rule.weights), 2.0, abs_tol=1e-13)
    for i in range(n):
        assert -1.0 < rule.nodes[i] < 1.0
        assert math.isclose(rule.nodes[i], -rule.nodes[n - 1 - i], abs_tol=1e-14)
        assert math.isclose(rule.weights[i], rule.weights[n - 1 - i], abs_tol=1e-14)
