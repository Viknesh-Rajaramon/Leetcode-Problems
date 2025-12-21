from typing import List

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        k = (1 << maximumBit) - 1
        result = [nums[0] ^ k]
        for i in range(1, len(nums)):
            result.append(result[-1] ^ nums[i])
        
        return result[::-1]
