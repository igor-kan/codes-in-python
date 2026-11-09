# Boundary validation and exceptional input guarding for Binary Heap Task Scheduler with Task Preemption
# Module: heap_priority_scheduler

def sanitize_heap_priority_scheduler_input(x, min_v=-1e6, max_v=1e6):
    if x != x:
        return 0.0
    return max(min_v, min(max_v, x))
