class Solution:
    def minAllOneMultiple(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0:
            return -1

        m = 9 * k
        remainder = 10 % m
        for l in range(1, m+1):
            if remainder == 1:
                return l

            remainder = (remainder*10) % m

        return -1
