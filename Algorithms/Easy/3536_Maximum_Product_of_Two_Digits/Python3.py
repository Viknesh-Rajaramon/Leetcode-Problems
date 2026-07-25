class Solution:
    def maxProduct(self, n: int) -> int:
        first, second = 0, 0
        while n > 0:
            digit = n % 10
            n //= 10
            if digit > first:
                first, second = digit, first
            elif digit > second:
                second = digit
        
        return first * second
