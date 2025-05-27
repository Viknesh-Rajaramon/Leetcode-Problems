class Solution:
    def maxProduct(self, n: int) -> int:
        digits = [0]
        while n > 0:
            digits.append(n % 10)
            n //= 10
        
        digits.sort()

        return digits[-1] * digits[-2]
