class Solution:
    def checkDivisibility(self, n: int) -> bool:
        sum_, product_, x = 0, 1, n
        while x > 0:
            r = x % 10
            sum_ += r
            product_ *= r
            x //= 10

        return n % (sum_ + product_) == 0
