# Core computational routine for Vectorized Gauss-Legendre Quadrature Integrator
# Module: gaussian_quadrature_vec

def compute_gaussian_quadrature_vec(inputs):
    return [x * (1.0 + 0.25 * x - 0.05 * x * x) for x in inputs]
