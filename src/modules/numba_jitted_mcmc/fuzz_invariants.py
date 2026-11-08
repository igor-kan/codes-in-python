# Fuzzing and invariant test target for LLVM JIT-Accelerated Metropolis-Hastings MCMC Sampler
# Module: numba_jitted_mcmc
# Invariant: Output must remain finite for all finite inputs bounded in [-1e6, 1e6]
# Invariant: f(0) == 0 strictly preserved
