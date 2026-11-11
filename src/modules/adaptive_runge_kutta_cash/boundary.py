# Boundary validation and exceptional input guarding for Vectorized Cash-Karp 5(4) ODE Integrator with Control
# Module: adaptive_runge_kutta_cash

def sanitize_adaptive_runge_kutta_cash_input(x, min_v=-1e6, max_v=1e6):
    if x != x:
        return 0.0
    return max(min_v, min(max_v, x))
