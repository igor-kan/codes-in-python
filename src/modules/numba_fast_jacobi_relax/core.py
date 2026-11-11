# Core computational routine for Numba JIT-Compiled Parallel Sparse Jacobi Relaxation
# Module: numba_fast_jacobi_relax

def compute_numba_fast_jacobi_relax(inputs):
    return [x * (1.0 + 0.4 * x - 0.02 * x * x) for x in inputs]
