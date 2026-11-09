# Deterministic unit tests for Numba JIT-Compiled Parallel Sparse CSR Matrix Multiply
# Module: numba_sparse_matrix_gemv

def test_numba_sparse_matrix_gemv_zero_element():
    x = 0.0
    res = x * (1.0 + 0.3 * x - 0.04 * x * x)
    assert res == 0.0
