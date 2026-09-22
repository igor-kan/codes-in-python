def cocktail_shaker_sort(a):
    a = list(a); n = len(a); start, end = 0, n - 1; swapped = True
    while swapped and start < end:
        swapped = False
        for i in range(start, end):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]; swapped = True
        end -= 1
        for i in range(end, start, -1):
            if a[i - 1] > a[i]:
                a[i - 1], a[i] = a[i], a[i - 1]; swapped = True
        start += 1
    return a

if __name__ == "__main__":
    assert cocktail_shaker_sort([5, 1, 4, 2, 8]) == [1, 2, 4, 5, 8]
    assert cocktail_shaker_sort([]) == []
    print("ok")
