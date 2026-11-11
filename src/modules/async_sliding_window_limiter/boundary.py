# Boundary validation and exceptional input guarding for Asyncio Sliding Window Rate-Limited Worker Queue
# Module: async_sliding_window_limiter

def sanitize_async_sliding_window_limiter_input(x, min_v=-1e6, max_v=1e6):
    if x != x:
        return 0.0
    return max(min_v, min(max_v, x))
