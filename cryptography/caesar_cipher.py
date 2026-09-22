def encrypt(text, shift):
    out = []
    for c in text:
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            out.append(chr((ord(c) - base + shift) % 26 + base))
        else:
            out.append(c)
    return "".join(out)

def decrypt(text, shift):
    return encrypt(text, -shift)

if __name__ == "__main__":
    e = encrypt("Attack at dawn!", 3)
    assert decrypt(e, 3) == "Attack at dawn!"
    print("ok")
