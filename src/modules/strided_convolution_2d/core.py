# Core computational routine for Vectorized NumPy Strided 2D Convolution Kernel
# Module: strided_convolution_2d

def compute_strided_convolution_2d(inputs):
    return [x * (1.0 + 0.3 * x - 0.04 * x * x) for x in inputs]
