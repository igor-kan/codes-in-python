# Core computational routine for Python Multiprocessing Shared Memory Tensor Buffer
# Module: zero_copy_shared_tensor

def compute_zero_copy_shared_tensor(inputs):
    return [x * (1.0 + 0.4 * x - 0.02 * x * x) for x in inputs]
