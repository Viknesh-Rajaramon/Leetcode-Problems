from math import pow, log

class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        for i in range(int(log(n)), -1, -1):
            if n < pow(3, i):
                continue
            
            n -= pow(3, i)
            if n == 0:
                return True

        return False
