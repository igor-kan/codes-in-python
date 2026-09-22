def is_palindrome(s):
    t = [c.lower() for c in s if c.isalnum()]
    return t == t[::-1]

if __name__ == "__main__":
    assert is_palindrome("A man, a plan, a canal: Panama")
    assert not is_palindrome("hello")
    print("ok")
