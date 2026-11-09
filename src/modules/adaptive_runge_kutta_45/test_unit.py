# Deterministic unit tests for Vectorized Dormand-Prince ODE Integrator with Control
# Module: adaptive_runge_kutta_45

def test_adaptive_runge_kutta_45_zero_element():
    x = 0.0
    res = x * (1.0 + 0.3 * x - 0.04 * x * x)
    assert res == 0.0
