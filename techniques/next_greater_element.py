def next_greater(a):
    res = [-1] * len(a); st = []
    for i, x in enumerate(a):
        while st and a[st[-1]] < x:
            res[st.pop()] = x
        st.append(i)
    return res

if __name__ == "__main__":
    assert next_greater([2, 1, 2, 4, 3]) == [4, 2, 4, -1, -1]
    print("ok")
