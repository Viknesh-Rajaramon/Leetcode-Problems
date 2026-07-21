from math import inf

class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        result, prev, n, i = 0, -inf, len(s), 0
        while i < n:
            start = i
            while i < n and s[i] == s[start]:
                i += 1
            
            if s[start] == "0":
                curr = i-start
                result = max(result, prev+curr)
                prev = curr

        return result + s.count("1")
