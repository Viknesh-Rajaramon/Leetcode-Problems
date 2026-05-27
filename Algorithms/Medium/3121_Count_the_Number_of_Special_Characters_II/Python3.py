class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower, upper = [-1] * 26, [-1] * 26
        for i, c in enumerate(word):
            if "a" <= c <= "z":
                lower[ord(c)-97] = i
            elif upper[ord(c)-65] == -1:
                upper[ord(c)-65] = i

        result = 0
        for i in range(26):
            if lower[i] != -1 and lower[i] < upper[i]:
                result += 1
        
        return result
