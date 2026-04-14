from typing import List

class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        result, prev = 0, 0
        for num in target:
            if num > prev:
                result += num - prev
            
            prev = num
        
        return result
