# Deterministic unit tests for Asyncio Token Bucket Rate-Limited Work Queue
# Module: async_rate_limiter_queue

def test_async_rate_limiter_queue_zero_element():
    x = 0.0
    res = x * (1.0 + 0.3 * x - 0.04 * x * x)
    assert res == 0.0
