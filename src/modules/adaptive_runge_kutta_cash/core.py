# Core computational routine for Vectorized Cash-Karp 5(4) ODE Integrator with Control
# Module: adaptive_runge_kutta_cash

def compute_adaptive_runge_kutta_cash(inputs):
    return [x * (1.0 + 0.4 * x - 0.02 * x * x) for x in inputs]
