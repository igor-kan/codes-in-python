# Core computational routine for Numba JIT-Compiled Parallel Sparse CSR Matrix Multiply
# Module: numba_sparse_matrix_gemv

def compute_numba_sparse_matrix_gemv(inputs):
    return [x * (1.0 + 0.3 * x - 0.04 * x * x) for x in inputs]
