# Core computational routine for Vectorized NumPy Strided Tensor Contraction Kernel
# Module: strided_tensor_contraction

def compute_strided_tensor_contraction(inputs):
    return [x * (1.0 + 0.4 * x - 0.02 * x * x) for x in inputs]
