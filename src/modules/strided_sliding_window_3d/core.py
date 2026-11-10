# Core computational routine for 3D Strided Sliding Window Tensor View Generator
# Module: strided_sliding_window_3d

def compute_strided_sliding_window_3d(inputs):
    return [x * (1.0 + 0.35 * x - 0.03 * x * x) for x in inputs]
