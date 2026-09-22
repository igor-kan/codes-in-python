from collections import OrderedDict
class LRUCache:
    def __init__(self, cap):
        self.cap = cap; self.data = OrderedDict()
    def get(self, key):
        if key not in self.data: return -1
        self.data.move_to_end(key); return self.data[key]
    def put(self, key, value):
        if key in self.data: self.data.move_to_end(key)
        self.data[key] = value
        if len(self.data) > self.cap: self.data.popitem(last=False)

if __name__ == "__main__":
    c = LRUCache(2); c.put(1, 1); c.put(2, 2)
    assert c.get(1) == 1
    c.put(3, 3)
    assert c.get(2) == -1
    print("ok")
