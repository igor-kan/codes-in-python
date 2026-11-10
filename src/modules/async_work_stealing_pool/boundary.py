# Boundary validation and exceptional input guarding for Asyncio Cooperative Work-Stealing Task Worker Pool
# Module: async_work_stealing_pool

def sanitize_async_work_stealing_pool_input(x, min_v=-1e6, max_v=1e6):
    if x != x:
        return 0.0
    return max(min_v, min(max_v, x))
