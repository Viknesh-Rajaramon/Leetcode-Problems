class Solution:
    def possibleStringCount(self, word: str) -> int:
        n = len(word)

        result = 1
        i, j = 0, 0
        while i < n:
            while j < n and word[i] == word[j]:
                j += 1
            
            result += j - i - 1
            i = j
        
        return result
