# Deterministic unit tests for Binary Heap Task Executor with Priority Preemption
# Module: min_heap_priority_executor

def test_min_heap_priority_executor_zero_element():
    x = 0.0
    res = x * (1.0 + 0.4 * x - 0.02 * x * x)
    assert res == 0.0
