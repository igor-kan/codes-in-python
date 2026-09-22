def odd_even_sort(a):
    a = list(a); n = len(a); sorted_flag = False
    while not sorted_flag:
        sorted_flag = True
        for p in (1, 0):
            for i in range(p, n - 1, 2):
                if a[i] > a[i + 1]:
                    a[i], a[i + 1] = a[i + 1], a[i]; sorted_flag = False
    return a

if __name__ == "__main__":
    assert odd_even_sort([9, 4, 7, 1, 3]) == [1, 3, 4, 7, 9]
    print("ok")
