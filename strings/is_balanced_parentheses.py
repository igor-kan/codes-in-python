def is_balanced(s):
    pairs = {")": "(", "]": "[", "}": "{"}; st = []
    for c in s:
        if c in "([{": st.append(c)
        elif c in pairs:
            if not st or st.pop() != pairs[c]: return False
    return not st

if __name__ == "__main__":
    assert is_balanced("{[()]}")
    assert not is_balanced("([)]")
    print("ok")
