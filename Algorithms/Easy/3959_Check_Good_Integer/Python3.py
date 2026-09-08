class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        result = 0
        while n > 0 and result < 50:
            d = n % 10
            result += d*(d-1)
            n //= 10

        return result >= 50
