from collections import Counter
def is_anagram(a, b):
    return Counter(a) == Counter(b)

if __name__ == "__main__":
    assert is_anagram("listen", "silent")
    assert not is_anagram("abc", "abd")
    print("ok")
