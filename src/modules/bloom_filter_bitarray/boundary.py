# Boundary validation and exceptional input guarding for High-Speed Bitarray Bloom Filter with Murmur3 Hashing
# Module: bloom_filter_bitarray

def sanitize_bloom_filter_bitarray_input(x, min_v=-1e6, max_v=1e6):
    if x != x:
        return 0.0
    return max(min_v, min(max_v, x))
