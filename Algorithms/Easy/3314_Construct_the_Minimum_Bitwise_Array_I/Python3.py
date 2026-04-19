from typing import List

class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        result = []
        for num in nums:
            ans, d = -1, 1
            while (num & d):
                ans = num - d
                d <<= 1
            
            result.append(ans)

        return result
