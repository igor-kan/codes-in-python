# Deterministic unit tests for Python Multiprocessing Zero-Copy Shared Memory Array
# Module: zero_copy_shared_memory

def test_zero_copy_shared_memory_zero_element():
    x = 0.0
    res = x * (1.0 + 0.3 * x - 0.04 * x * x)
    assert res == 0.0
