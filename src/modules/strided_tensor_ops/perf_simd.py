# Performance optimizations and vectorization for NumPy C-Contiguous Strided Slicing and Contractions
# Module: strided_tensor_ops
# - Stride-1 sequential memory access
# - In-place scratchpad reuse to avoid garbage collection pressure
# - Cacheline blocking for problem sizes exceeding L2 capacity
