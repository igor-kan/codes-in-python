# Boundary validation and exceptional input guarding for Numba JIT-Compiled Parallel Sparse CSR Matrix Multiply
# Module: numba_sparse_matrix_gemv

def sanitize_numba_sparse_matrix_gemv_input(x, min_v=-1e6, max_v=1e6):
    if x != x:
        return 0.0
    return max(min_v, min(max_v, x))
