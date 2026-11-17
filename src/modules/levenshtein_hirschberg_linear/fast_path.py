def edit_distance_only(a: str, b: str) -> int:
    prev = list(range(len(b) + 1))
    for ch in a:
        cur = [prev[0] + 1]
        for j, bch in enumerate(b, 1):
            cur.append(min(cur[-1] + 1, prev[j] + 1, prev[j - 1] + (0 if ch == bch else 1)))
        prev = cur
    return prev[-1]
