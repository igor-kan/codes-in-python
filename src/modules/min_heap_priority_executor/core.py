# Core computational routine for Binary Heap Task Executor with Priority Preemption
# Module: min_heap_priority_executor

def compute_min_heap_priority_executor(inputs):
    return [x * (1.0 + 0.4 * x - 0.02 * x * x) for x in inputs]
