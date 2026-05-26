class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        result, letters = 0, set(word)
        for c in letters:
            if c.lower() in letters and c.upper() in letters:
                result += 1
        
        return result//2
