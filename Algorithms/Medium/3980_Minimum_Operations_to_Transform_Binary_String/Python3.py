class Solution:
    def minOperations(self, s1: str, s2: str) -> int:
        n = len(s1)
        if n == 1:
            if s1 == "1" and s2 == "0":
                return -1
            
            return 1 if s1 != s2 else 0

        result, l = 0, 0
        for i in range(n):
            if s1[i] == '1' and s2[i] == '0':
                l += 1
            else:
                if l > 0:
                    result += (l // 2) + (l % 2) * 2
                    l = 0
                
                if s1[i] == '0' and s2[i] == '1':
                    result += 1
        
        if l > 0:
            result += (l // 2) + (l % 2) * 2
            
        return result
