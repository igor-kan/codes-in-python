# Boundary validation and exceptional input handling for LLVM JIT-Accelerated Metropolis-Hastings MCMC Sampler
# Module: numba_jitted_mcmc
# - Guards against NaN and Infinite values
# - Clamps domain boundaries within mathematically permissible intervals
# - Graceful error propagation
