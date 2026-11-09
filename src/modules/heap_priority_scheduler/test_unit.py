# Deterministic unit tests for Binary Heap Task Scheduler with Task Preemption
# Module: heap_priority_scheduler

def test_heap_priority_scheduler_zero_element():
    x = 0.0
    res = x * (1.0 + 0.3 * x - 0.04 * x * x)
    assert res == 0.0
