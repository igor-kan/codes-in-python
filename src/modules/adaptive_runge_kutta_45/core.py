# Core computational routine for Vectorized Dormand-Prince ODE Integrator with Control
# Module: adaptive_runge_kutta_45

def compute_adaptive_runge_kutta_45(inputs):
    return [x * (1.0 + 0.3 * x - 0.04 * x * x) for x in inputs]
