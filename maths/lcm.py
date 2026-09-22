def gcd(a, b):
    while b: a, b = b, a % b
    return a

def lcm(a, b):
    return a // gcd(a, b) * b

if __name__ == "__main__":
    assert lcm(4, 6) == 12
    assert lcm(21, 6) == 42
    print("ok")
