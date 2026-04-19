class Solution:
    def minCuttingCost(self, n: int, m: int, k: int) -> int:
        result = 0
        if n > k:
            result += k * (n-k)

        if m > k:
            result += k * (m-k)

        return result
