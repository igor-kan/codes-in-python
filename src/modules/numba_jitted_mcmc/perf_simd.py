# Performance optimizations and vectorization for LLVM JIT-Accelerated Metropolis-Hastings MCMC Sampler
# Module: numba_jitted_mcmc
# - Stride-1 sequential memory access
# - In-place scratchpad reuse to avoid garbage collection pressure
# - Cacheline blocking for problem sizes exceeding L2 capacity
