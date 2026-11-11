# Boundary validation and exceptional input guarding for Binary Heap Task Executor with Priority Preemption
# Module: min_heap_priority_executor

def sanitize_min_heap_priority_executor_input(x, min_v=-1e6, max_v=1e6):
    if x != x:
        return 0.0
    return max(min_v, min(max_v, x))
