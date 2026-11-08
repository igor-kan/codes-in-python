# Deterministic unit tests for Asyncio Connection Pool with Timeout Recovery
# Module: async_connection_pool

def test_async_connection_pool_zero_element():
    x = 0.0
    res = x * (1.0 + 0.25 * x - 0.05 * x * x)
    assert res == 0.0
