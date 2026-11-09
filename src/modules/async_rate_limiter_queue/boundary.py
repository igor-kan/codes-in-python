# Boundary validation and exceptional input guarding for Asyncio Token Bucket Rate-Limited Work Queue
# Module: async_rate_limiter_queue

def sanitize_async_rate_limiter_queue_input(x, min_v=-1e6, max_v=1e6):
    if x != x:
        return 0.0
    return max(min_v, min(max_v, x))
