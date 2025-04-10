class Trie:

    def __init__(self):
        self.data = set()
        self.words = set()
        
    # Inserts the string word into the trie.
    def insert(self, word: str) -> None:
        tmp = ''
        for ch in word:
            tmp += ch
            self.data.add(tmp)
        self.words.add(word)

    def search(self, word: str) -> bool:
        if word in self.words:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        if prefix in self.data:
            return True
        return False


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)