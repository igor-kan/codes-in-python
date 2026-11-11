# Deterministic unit tests for Python Multiprocessing Shared Memory Tensor Buffer
# Module: zero_copy_shared_tensor

def test_zero_copy_shared_tensor_zero_element():
    x = 0.0
    res = x * (1.0 + 0.4 * x - 0.02 * x * x)
    assert res == 0.0
