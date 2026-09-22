def _shift(c, k, dec=False):
    if not c.isalpha(): return c
    base = ord('A') if c.isupper() else ord('a')
    s = (ord(c) - base + (-k if dec else k)) % 26
    return chr(s + base)

def encrypt(text, key):
    key = [ord(c.lower()) - 97 for c in key if c.isalpha()]
    return "".join(_shift(c, key[i % len(key)]) for i, c in enumerate(text) if key) if key else text

def decrypt(text, key):
    key = [ord(c.lower()) - 97 for c in key if c.isalpha()]
    return "".join(_shift(c, key[i % len(key)], True) for i, c in enumerate(text) if key) if key else text

if __name__ == "__main__":
    e = encrypt("HELLO", "KEY")
    assert decrypt(e, "KEY") == "HELLO"
    print("ok")
