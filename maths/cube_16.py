"""Cube of 16."""

def cube(n):
    return n * n * n

if __name__ == "__main__":
    assert cube(16) == 4096
    print("ok")
