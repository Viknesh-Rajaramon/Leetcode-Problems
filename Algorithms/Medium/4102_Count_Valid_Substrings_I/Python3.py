class Solution:
    def countValidSubstrings(self, s: str) -> int:
        result, l = 0, 0
        for r in range(len(s)):
            if r >= 2 and s[r-2 : r+1] == "abc":
                l = r-1
            
            result += r-l+1

        return result
