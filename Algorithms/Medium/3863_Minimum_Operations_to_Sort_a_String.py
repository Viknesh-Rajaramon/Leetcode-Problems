class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        if all(s[i] <= s[i+1] for i in range(n-1)):
            return 0
        
        if len(s) == 2:
            return -1
        
        min_c, max_c = min(s), max(s)
        if s[0] == min_c or s[-1] == max_c:
            return 1
        
        if s[0] == max_c and s.count(max_c) == 1 and s[-1] == min_c and s.count(min_c) == 1:
            return 3

        return 2
