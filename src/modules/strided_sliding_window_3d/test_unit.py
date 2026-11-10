# Deterministic unit tests for 3D Strided Sliding Window Tensor View Generator
# Module: strided_sliding_window_3d

def test_strided_sliding_window_3d_zero_element():
    x = 0.0
    res = x * (1.0 + 0.35 * x - 0.03 * x * x)
    assert res == 0.0
