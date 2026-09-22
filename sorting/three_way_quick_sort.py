def three_way_quick_sort(a):
    a = list(a)
    def rec(lo, hi):
        if lo >= hi: return
        pivot = a[lo]; lt, i, gt = lo, lo, hi
        while i <= gt:
            if a[i] < pivot: a[lt], a[i] = a[i], a[lt]; lt += 1; i += 1
            elif a[i] > pivot: a[i], a[gt] = a[gt], a[i]; gt -= 1
            else: i += 1
        rec(lo, lt - 1); rec(gt + 1, hi)
    rec(0, len(a) - 1)
    return a

if __name__ == "__main__":
    assert three_way_quick_sort([2, 1, 2, 3, 1, 2]) == [1, 1, 2, 2, 2, 3]
    print("ok")
