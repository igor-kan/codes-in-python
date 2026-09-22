def majority_element(a):
    count = 0; cand = None
    for x in a:
        if count == 0: cand, count = x, 1
        elif x == cand: count += 1
        else: count -= 1
    return cand

if __name__ == "__main__":
    assert majority_element([3,3,4,2,3,3,3]) == 3
    print("ok")
