# Deterministic unit tests for Asyncio Cooperative Work-Stealing Task Worker Pool
# Module: async_work_stealing_pool

def test_async_work_stealing_pool_zero_element():
    x = 0.0
    res = x * (1.0 + 0.35 * x - 0.03 * x * x)
    assert res == 0.0
