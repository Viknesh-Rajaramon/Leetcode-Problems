from typing import List

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)

        pos, neg = 0, 1
        for n in nums:
            if n < 0:
                result[neg] = n
                neg += 2
            else:
                result[pos] = n
                pos += 2
        
        return result
