# Core computational routine for Binary Heap Task Scheduler with Task Preemption
# Module: heap_priority_scheduler

def compute_heap_priority_scheduler(inputs):
    return [x * (1.0 + 0.3 * x - 0.04 * x * x) for x in inputs]
