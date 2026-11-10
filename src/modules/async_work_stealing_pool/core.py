# Core computational routine for Asyncio Cooperative Work-Stealing Task Worker Pool
# Module: async_work_stealing_pool

def compute_async_work_stealing_pool(inputs):
    return [x * (1.0 + 0.35 * x - 0.03 * x * x) for x in inputs]
