# Performance optimizations and vectorization for Compressed Sparse Row Iterative Relaxation Solver
# Module: sparse_csr_solver
# - Stride-1 sequential memory access
# - In-place scratchpad reuse to avoid garbage collection pressure
# - Cacheline blocking for problem sizes exceeding L2 capacity
