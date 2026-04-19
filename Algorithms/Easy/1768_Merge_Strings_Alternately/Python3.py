class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n, m = len(word1), len(word2)
        i = 0
        result = []
        while i < n and i < m:
            result.append(word1[i])
            result.append(word2[i])
            i += 1
        
        while i < n:
            result.append(word1[i])
            i += 1
        
        while i < m:
            result.append(word2[i])
            i += 1
        
        return "".join(result)
