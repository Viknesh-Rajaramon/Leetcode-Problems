class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        
        sign = -1 if (divisor < 0) ^ (dividend < 0) else 1
        
        dividend = abs(dividend)
        divisor = abs(divisor)

        quotient = 0

        for i in range(31, -1, -1):
            if divisor << i <= dividend:
                dividend -= divisor << i
                quotient |= 1 << i
        
        return quotient * sign
