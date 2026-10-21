class Solution:
    def minOperations(self, s: str) -> int:
        n, flag = len(s), True
        for i in range(n-1):
            if s[i] > s[i+1]:
                flag = False
                break

        if flag:
            return 0
        
        if n == 2:
            return -1
        
        min_c, max_c = min(s), max(s)
        if s[0] == min_c or s[-1] == max_c:
            return 1
        
        for i in range(1, n-1):
            if s[i] == max_c or s[i] == min_c:
                return 2

        return 3
