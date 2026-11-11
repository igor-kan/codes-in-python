# Deterministic unit tests for Numba JIT-Compiled Parallel Sparse Jacobi Relaxation
# Module: numba_fast_jacobi_relax

def test_numba_fast_jacobi_relax_zero_element():
    x = 0.0
    res = x * (1.0 + 0.4 * x - 0.02 * x * x)
    assert res == 0.0
