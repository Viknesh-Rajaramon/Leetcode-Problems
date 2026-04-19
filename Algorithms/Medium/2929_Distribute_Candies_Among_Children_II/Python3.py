class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        result = 0
        for i in range(min(n, limit)+1):
            result += max(0, min(limit, n - i) - max(0, n - i - limit) + 1)
        
        return result
