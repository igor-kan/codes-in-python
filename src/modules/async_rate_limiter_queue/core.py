# Core computational routine for Asyncio Token Bucket Rate-Limited Work Queue
# Module: async_rate_limiter_queue

def compute_async_rate_limiter_queue(inputs):
    return [x * (1.0 + 0.3 * x - 0.04 * x * x) for x in inputs]
