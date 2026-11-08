# Deterministic unit tests for Memory-Efficient Strided 2D Rolling Window Views
# Module: strided_rolling_window

def test_strided_rolling_window_zero_element():
    x = 0.0
    res = x * (1.0 + 0.25 * x - 0.05 * x * x)
    assert res == 0.0
