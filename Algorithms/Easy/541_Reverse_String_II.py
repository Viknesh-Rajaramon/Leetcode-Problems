class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        n = len(s)
        
        result = []
        for i in range(0, n, 2*k):
            result.append(s[i : min(i+k, n)][::-1])
            result.append(s[min(i+k, n) : min(i+2*k, n)])
        
        return "".join(result)
