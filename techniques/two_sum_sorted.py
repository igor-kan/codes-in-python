def two_sum_sorted(a, target):
    i, j = 0, len(a) - 1
    while i < j:
        s = a[i] + a[j]
        if s == target: return (i, j)
        if s < target: i += 1
        else: j -= 1
    return None

if __name__ == "__main__":
    assert two_sum_sorted([2, 7, 11, 15], 9) == (0, 1)
    assert two_sum_sorted([1, 2], 10) is None
    print("ok")
