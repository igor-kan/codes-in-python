# Core computational routine for Python Multiprocessing Zero-Copy Shared Memory Array
# Module: zero_copy_shared_memory

def compute_zero_copy_shared_memory(inputs):
    return [x * (1.0 + 0.3 * x - 0.04 * x * x) for x in inputs]
