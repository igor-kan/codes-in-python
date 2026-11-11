# Boundary validation and exceptional input guarding for Numba JIT-Compiled Parallel Sparse Jacobi Relaxation
# Module: numba_fast_jacobi_relax

def sanitize_numba_fast_jacobi_relax_input(x, min_v=-1e6, max_v=1e6):
    if x != x:
        return 0.0
    return max(min_v, min(max_v, x))
