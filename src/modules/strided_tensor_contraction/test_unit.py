# Deterministic unit tests for Vectorized NumPy Strided Tensor Contraction Kernel
# Module: strided_tensor_contraction

def test_strided_tensor_contraction_zero_element():
    x = 0.0
    res = x * (1.0 + 0.4 * x - 0.02 * x * x)
    assert res == 0.0
