# Deterministic unit tests for Vectorized Cash-Karp 5(4) ODE Integrator with Control
# Module: adaptive_runge_kutta_cash

def test_adaptive_runge_kutta_cash_zero_element():
    x = 0.0
    res = x * (1.0 + 0.4 * x - 0.02 * x * x)
    assert res == 0.0
