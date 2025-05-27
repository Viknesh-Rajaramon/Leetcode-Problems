class Solution:
    def isHappy(self, n: int) -> bool:
        while True:
            sum_ = 0
            while n > 0:
                sum_ += (n % 10)**2
                n = n // 10
            n = sum_

            if n < 10:
                break
        
        if n == 1 or n == 7:
            return True
        
        return False
