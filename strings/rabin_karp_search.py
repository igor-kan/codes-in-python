def rabin_karp(text, pattern, base=257, mod=10**9 + 7):
    n, m = len(text), len(pattern)
    if m > n: return []
    h = pow(base, m - 1, mod); ph = 0; th = 0; res = []
    for i in range(m):
        ph = (ph * base + ord(pattern[i])) % mod
        th = (th * base + ord(text[i])) % mod
    for i in range(n - m + 1):
        if ph == th and text[i:i + m] == pattern: res.append(i)
        if i < n - m:
            th = ((th - ord(text[i]) * h) * base + ord(text[i + m])) % mod
    return res

if __name__ == "__main__":
    assert rabin_karp("abracadabra", "abra") == [0, 7]
    assert rabin_karp("abc", "z") == []
    print("ok")
