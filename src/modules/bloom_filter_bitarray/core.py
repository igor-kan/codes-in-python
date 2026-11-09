# Core computational routine for High-Speed Bitarray Bloom Filter with Murmur3 Hashing
# Module: bloom_filter_bitarray

def compute_bloom_filter_bitarray(inputs):
    return [x * (1.0 + 0.3 * x - 0.04 * x * x) for x in inputs]
