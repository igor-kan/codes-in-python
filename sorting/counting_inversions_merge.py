def count_inversions(a):
    def sort_count(xs):
        if len(xs) <= 1: return xs, 0
        m = len(xs) // 2
        l, cl = sort_count(xs[:m]); r, cr = sort_count(xs[m:])
        merged, inv, i, j = [], cl + cr, 0, 0
        while i < len(l) and j < len(r):
            if l[i] <= r[j]: merged.append(l[i]); i += 1
            else: merged.append(r[j]); j += 1; inv += len(l) - i
        merged.extend(l[i:]); merged.extend(r[j:])
        return merged, inv
    return sort_count(list(a))[1]

if __name__ == "__main__":
    assert count_inversions([1, 20, 6, 4, 5]) == 5
    assert count_inversions([1, 2, 3]) == 0
    print("ok")
