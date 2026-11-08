# Boundary validation and exceptional input guarding for Asyncio Connection Pool with Timeout Recovery
# Module: async_connection_pool

def sanitize_async_connection_pool_input(x, min_b=-1e6, max_b=1e6):
    if x != x:  # NaN guard
        return 0.0
    return max(min_b, min(max_b, x))
