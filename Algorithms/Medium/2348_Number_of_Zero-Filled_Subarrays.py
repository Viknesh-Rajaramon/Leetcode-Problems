from typing import List

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        result = 0
        
        length = 0
        for num in nums:
            if num == 0:
                length += 1
            elif length > 0:
                result += length * (length+1) // 2
                length = 0

        if length > 0:
            result += length * (length+1) // 2
        
        return result
