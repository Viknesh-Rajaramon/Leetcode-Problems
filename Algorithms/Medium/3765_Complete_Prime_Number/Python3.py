from math import sqrt

class Solution:
    def completePrime(self, num: int) -> bool:
        def is_prime(n: int) -> bool:
            if n == 1:
                return False

            for i in range(2, int(sqrt(n))+1):
                if n % i == 0:
                    return False
            
            return True
        
        x, y, z = num, 0, 1
        while x > 0:
            y += z * (x % 10)
            if not is_prime(x) or not is_prime(y):
                return False
            
            x //= 10
            z *= 10

        return True
