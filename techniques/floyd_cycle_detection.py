def has_cycle_next(next_fn, start):
    slow = fast = start
    while True:
        slow = next_fn(slow)
        fast = next_fn(next_fn(fast))
        if slow is None or fast is None or next_fn(fast) is None: return False
        if slow == fast: return True

if __name__ == "__main__":
    nxt = {1: 2, 2: 3, 3: 4, 4: 2}
    assert has_cycle_next(lambda x: nxt.get(x), 1)
    nxt2 = {1: 2, 2: 3, 3: None}
    assert not has_cycle_next(lambda x: nxt2.get(x), 1)
    print("ok")
