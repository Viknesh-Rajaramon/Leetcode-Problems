class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False

        num = bin(n)[2 : ]
        return num.count("1") == 1 and num.count("0") % 2 == 0
