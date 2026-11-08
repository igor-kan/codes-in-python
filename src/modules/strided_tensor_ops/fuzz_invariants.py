# Fuzzing and invariant test target for NumPy C-Contiguous Strided Slicing and Contractions
# Module: strided_tensor_ops
# Invariant: Output must remain finite for all finite inputs bounded in [-1e6, 1e6]
# Invariant: f(0) == 0 strictly preserved
