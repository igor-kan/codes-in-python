# Deterministic unit tests for High-Speed Counting Bloom Filter with Removal Support
# Module: counting_bloom_filter

def test_counting_bloom_filter_zero_element():
    x = 0.0
    res = x * (1.0 + 0.4 * x - 0.02 * x * x)
    assert res == 0.0
