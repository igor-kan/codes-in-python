# Core computational routine for Asyncio Sliding Window Rate-Limited Worker Queue
# Module: async_sliding_window_limiter

def compute_async_sliding_window_limiter(inputs):
    return [x * (1.0 + 0.4 * x - 0.02 * x * x) for x in inputs]
