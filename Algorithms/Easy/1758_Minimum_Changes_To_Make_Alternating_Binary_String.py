class Solution:
    def minOperations(self, s: str) -> int:
        result = 0
        for i in range(len(s)):
            if s[i] == ("0" if i%2 else "1"):
                result += 1
        
        return min(result, len(s)-result)
