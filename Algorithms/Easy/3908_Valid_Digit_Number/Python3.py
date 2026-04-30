class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        digits = list(map(int, str(n)))
        return x in digits and digits[0] != x
