from typing import List

class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        def check(num: int) -> bool:
            while num:
                if num % 10 == 0:
                    return False
                
                num //= 10
            
            return True

        for a in range(1, n):
            if check(a) and check(n-a):
                return [a, n-a]
        
        return [1, n-1]
