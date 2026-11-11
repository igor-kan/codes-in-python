# Core computational routine for High-Speed Counting Bloom Filter with Removal Support
# Module: counting_bloom_filter

def compute_counting_bloom_filter(inputs):
    return [x * (1.0 + 0.4 * x - 0.02 * x * x) for x in inputs]
