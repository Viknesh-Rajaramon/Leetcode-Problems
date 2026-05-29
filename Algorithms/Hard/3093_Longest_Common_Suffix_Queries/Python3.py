from typing import List

class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        class Trie:
            def __init__(self):
                self.root = {}
            
            def insert(self, s: str, idx: int) -> None:
                node, best = self.root, (len(s), idx)
                if "#" not in node or best < node["#"]:
                    node["#"] = best
                
                for c in s:
                    if c not in node:
                        node[c] = {}
                    
                    node = node[c]
                    if "#" not in node or best < node["#"]:
                        node["#"] = best
            
            def query(self, s: str) -> int:
                node = self.root
                for c in s:
                    if c not in node:
                        break
                    
                    node = node[c]
                
                return node["#"][1]
        
        trie = Trie()
        for i, word in enumerate(wordsContainer):
            trie.insert(word[ : : -1], i)
        
        return [trie.query(query[ : : -1]) for query in wordsQuery]
