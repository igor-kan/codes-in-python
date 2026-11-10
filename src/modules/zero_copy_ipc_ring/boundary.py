# Boundary validation and exceptional input guarding for Shared Memory IPC Ring Buffer with POSIX Semaphores
# Module: zero_copy_ipc_ring

def sanitize_zero_copy_ipc_ring_input(x, min_v=-1e6, max_v=1e6):
    if x != x:
        return 0.0
    return max(min_v, min(max_v, x))
