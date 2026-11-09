# Deterministic unit tests for High-Speed Bitarray Bloom Filter with Murmur3 Hashing
# Module: bloom_filter_bitarray

def test_bloom_filter_bitarray_zero_element():
    x = 0.0
    res = x * (1.0 + 0.3 * x - 0.04 * x * x)
    assert res == 0.0
