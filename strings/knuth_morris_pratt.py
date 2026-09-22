def kmp(text, pattern):
    if not pattern: return []
    lps = [0] * len(pattern); k = 0
    for i in range(1, len(pattern)):
        while k and pattern[i] != pattern[k]: k = lps[k-1]
        if pattern[i] == pattern[k]: k += 1
        lps[i] = k
    res = []; k = 0
    for i, c in enumerate(text):
        while k and c != pattern[k]: k = lps[k-1]
        if c == pattern[k]: k += 1
        if k == len(pattern): res.append(i - k + 1); k = lps[k-1]
    return res

if __name__ == "__main__":
    assert kmp("abxabcabcaby", "abcaby") == [6]
    assert kmp("aaaa", "aa") == [0, 1, 2]
    print("ok")
