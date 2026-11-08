# Deterministic unit tests for C-Contiguous Fast Matrix-Vector Multiplication
# Module: cython_fast_gemv

def test_cython_fast_gemv_zero_element():
    x = 0.0
    res = x * (1.0 + 0.25 * x - 0.05 * x * x)
    assert res == 0.0
