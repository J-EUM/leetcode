class Trie:

    def __init__(self):
        self.d = {}
        
    # Inserts the string word into the trie.
    def insert(self, word: str) -> None:
        temp = self.d
        for ch in word:
            if ch not in temp:
                temp[ch] = {}
            temp = temp[ch] 
        temp["end"] = True

    def search(self, word: str) -> bool:
        temp = self.d
        for ch in word:
            if ch not in temp:
                return False
            temp = temp[ch]
        return "end" in temp

    def startsWith(self, prefix: str) -> bool:
        temp = self.d
        for ch in prefix:
            if ch not in temp:
                return False
            temp = temp[ch]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)