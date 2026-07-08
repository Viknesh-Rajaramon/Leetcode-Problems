class Solution:
    def consecutiveSetBits(self, n: int) -> bool:
        n = n & (n >> 1)
        return n > 0 and not (n & (n-1))
