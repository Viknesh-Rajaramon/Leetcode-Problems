from typing import List

class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        result, rem = [], 0
        for i in nums:
            rem = (rem*2 + i) % 5
            result.append(rem == 0)

        return result
