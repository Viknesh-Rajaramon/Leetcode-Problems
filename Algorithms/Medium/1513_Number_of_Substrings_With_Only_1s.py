class Solution:
    def numSub(self, s: str) -> int:
        result = 0
        for sub in s.split("0"):
            n = len(sub)
            result += n * (n + 1)
        
        return (result // 2) % (10**9+7)
