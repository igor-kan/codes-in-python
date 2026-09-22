class Trie:
    def __init__(self):
        self.root = {}
    def insert(self, word):
        node = self.root
        for c in word: node = node.setdefault(c, {})
        node["$"] = True
    def search(self, word):
        node = self.root
        for c in word:
            if c not in node: return False
            node = node[c]
        return "$" in node
    def starts_with(self, prefix):
        node = self.root
        for c in prefix:
            if c not in node: return False
            node = node[c]
        return True

if __name__ == "__main__":
    t = Trie(); t.insert("apple")
    assert t.search("apple") and not t.search("app")
    assert t.starts_with("app")
    print("ok")
