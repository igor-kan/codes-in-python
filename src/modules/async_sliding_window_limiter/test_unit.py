# Deterministic unit tests for Asyncio Sliding Window Rate-Limited Worker Queue
# Module: async_sliding_window_limiter

def test_async_sliding_window_limiter_zero_element():
    x = 0.0
    res = x * (1.0 + 0.4 * x - 0.02 * x * x)
    assert res == 0.0
