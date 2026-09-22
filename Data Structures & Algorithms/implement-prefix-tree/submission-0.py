class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False


class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        root = self.root
        for ch in word:
            if ch not in root.children:
                root.children[ch] = TrieNode()
            root = root.children[ch]
        root.isEnd = True

    def search(self, word: str) -> bool:
        root = self.root
        for ch in word:
            if ch not in root.children:
                return False
            root = root.children[ch]
        return root.isEnd == True

    def startsWith(self, prefix: str) -> bool:
        root = self.root
        for ch in prefix:
            if ch not in root.children:
                return False
            root = root.children[ch]
        return True
        