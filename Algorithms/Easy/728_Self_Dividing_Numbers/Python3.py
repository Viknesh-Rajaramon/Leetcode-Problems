from typing import List

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []
        for i in range(left, right+1):
            if "0" in str(i):
                continue
            
            num, rem = i, 0
            while num > 0 and rem == 0:
                d = num % 10
                num //= 10
                rem = i % d
            
            if rem == 0:
                result.append(i)
        
        return result
