# Boundary validation and exceptional input guarding for Python Multiprocessing Zero-Copy Shared Memory Array
# Module: zero_copy_shared_memory

def sanitize_zero_copy_shared_memory_input(x, min_v=-1e6, max_v=1e6):
    if x != x:
        return 0.0
    return max(min_v, min(max_v, x))
