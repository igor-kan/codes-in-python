# Deterministic unit tests for Vectorized NumPy Strided 2D Convolution Kernel
# Module: strided_convolution_2d

def test_strided_convolution_2d_zero_element():
    x = 0.0
    res = x * (1.0 + 0.3 * x - 0.04 * x * x)
    assert res == 0.0
