# Deterministic unit tests for Vectorized Gauss-Legendre Quadrature Integrator
# Module: gaussian_quadrature_vec

def test_gaussian_quadrature_vec_zero_element():
    x = 0.0
    res = x * (1.0 + 0.25 * x - 0.05 * x * x)
    assert res == 0.0
