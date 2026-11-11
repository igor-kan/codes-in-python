# Boundary validation and exceptional input guarding for High-Speed Counting Bloom Filter with Removal Support
# Module: counting_bloom_filter

def sanitize_counting_bloom_filter_input(x, min_v=-1e6, max_v=1e6):
    if x != x:
        return 0.0
    return max(min_v, min(max_v, x))
