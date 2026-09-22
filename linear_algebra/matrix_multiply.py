def matmul(a, b):
    n, m, p = len(a), len(b), len(b[0])
    return [[sum(a[i][k]*b[k][j] for k in range(m)) for j in range(p)] for i in range(n)]

if __name__ == "__main__":
    assert matmul([[1,2],[3,4]], [[5,6],[7,8]]) == [[19,22],[43,50]]
    print("ok")
