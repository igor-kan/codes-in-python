class MinStack:
    def __init__(self):
        self.stack = []; self.mins = []
    def push(self, x):
        self.stack.append(x)
        self.mins.append(x if not self.mins else min(x, self.mins[-1]))
    def pop(self):
        self.mins.pop(); return self.stack.pop()
    def top(self): return self.stack[-1]
    def get_min(self): return self.mins[-1]

if __name__ == "__main__":
    s = MinStack(); s.push(3); s.push(1); s.push(2)
    assert s.get_min() == 1
    s.pop(); assert s.get_min() == 1
    s.pop(); assert s.get_min() == 3
    print("ok")
