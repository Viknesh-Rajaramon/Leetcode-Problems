from typing import List

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            s = set()
            for i in range(1, int(num**0.5)+1):
                if num%i == 0:
                    s.add(i)
                    s.add(num//i)
                
                    if len(s) > 4:
                        break
                
            if len(s) == 4:
                result += sum(s)
        
        return result
