class Solution:
    def countCommas(self, n: int) -> int:
        result, divisor = 0, 1000
        while n >= divisor:
            result += n-divisor+1
            divisor *= 1000

        return result
