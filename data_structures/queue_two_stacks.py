class Queue:
    def __init__(self):
        self.inn = []; self.out = []
    def push(self, x): self.inn.append(x)
    def pop(self):
        if not self.out:
            while self.inn: self.out.append(self.inn.pop())
        return self.out.pop()
    def peek(self):
        if not self.out:
            while self.inn: self.out.append(self.inn.pop())
        return self.out[-1]
    def empty(self): return not self.inn and not self.out

if __name__ == "__main__":
    q = Queue(); q.push(1); q.push(2)
    assert q.peek() == 1 and q.pop() == 1 and not q.empty()
    print("ok")
