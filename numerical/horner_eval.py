def horner(coeffs, x):
    acc = 0
    for c in coeffs: acc = acc * x + c
    return acc

if __name__ == "__main__":
    assert horner([1, -3, 2], 2) == 0
    assert horner([2, 0, 1], 3) == 19
    print("ok")
