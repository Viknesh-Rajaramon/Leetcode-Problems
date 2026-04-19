class WordDictionary:

    def __init__(self):
        self.trie = {}
        self.end_str = "*"

    def addWord(self, word: str) -> None:
        curr = self.trie
        for c in word:
            if c not in curr:
                curr[c] = {}
            
            curr = curr[c]
        
        curr[self.end_str] = ""

    def search(self, word: str) -> bool:
        def dfs(i: int, curr: dict) -> bool:
            if i == len(word):
                return self.end_str in curr
            
            if word[i] != ".":
                if word[i] not in curr:
                    return False
                
                return dfs(i+1, curr[word[i]])
            
            for c in curr:
                if dfs(i+1, curr[c]):
                    return True
            
            return False

        return dfs(0, self.trie)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
