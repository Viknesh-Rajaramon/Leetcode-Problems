class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        sum_1 = n * (n + 1) // 2
        x = n // m
        sum_2 = (x * (x + 1) // 2) * m * 2

        return sum_1 - sum_2
