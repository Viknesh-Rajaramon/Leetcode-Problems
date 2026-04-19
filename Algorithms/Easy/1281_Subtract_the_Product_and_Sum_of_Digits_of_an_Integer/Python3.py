class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum_, product = 0, 1
        while n > 0:
            d = n % 10
            product *= d
            sum_ += d
            n //= 10
        
        return product - sum_
