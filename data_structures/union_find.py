class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n)); self.rank = [0] * n
    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]; x = self.parent[x]
        return x
    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb: return False
        if self.rank[ra] < self.rank[rb]: ra, rb = rb, ra
        self.parent[rb] = ra
        if self.rank[ra] == self.rank[rb]: self.rank[ra] += 1
        return True

if __name__ == "__main__":
    uf = UnionFind(5)
    assert uf.union(0, 1) and uf.find(0) == uf.find(1)
    assert not uf.union(0, 1)
    print("ok")
