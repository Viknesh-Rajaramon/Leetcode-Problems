from imports import *

class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        def digits(num) -> List[int]:
            d = []
            while num > 0:
                d.append(num % 10)
                num //= 10
            
            return [0] * (4 - len(d)) + d[::-1]
        
        num1, num2, num3 = digits(num1), digits(num2), digits(num3)
        key = 0
        for i in range(4):
            key = key * 10 + min(num1[i], num2[i], num3[i])
        
        return key
