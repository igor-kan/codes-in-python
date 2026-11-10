# Core computational routine for Shared Memory IPC Ring Buffer with POSIX Semaphores
# Module: zero_copy_ipc_ring

def compute_zero_copy_ipc_ring(inputs):
    return [x * (1.0 + 0.35 * x - 0.03 * x * x) for x in inputs]
