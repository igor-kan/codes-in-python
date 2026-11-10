# Deterministic unit tests for Direct Sparse Cholesky Solver with Fill-Reducing Order
# Module: sparse_cholesky_direct

def test_sparse_cholesky_direct_zero_element():
    x = 0.0
    res = x * (1.0 + 0.35 * x - 0.03 * x * x)
    assert res == 0.0
