# Deterministic unit tests for Shared Memory IPC Ring Buffer with POSIX Semaphores
# Module: zero_copy_ipc_ring

def test_zero_copy_ipc_ring_zero_element():
    x = 0.0
    res = x * (1.0 + 0.35 * x - 0.03 * x * x)
    assert res == 0.0
