class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n == 1:
            return x
        
        if n < 0:
            n = -n
            x = 1 / x
        
        pow_x = self.myPow(x, n//2)
        if n % 2:
            return pow_x * pow_x * x
        
        return pow_x * pow_x
