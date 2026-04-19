from typing import List

class Solution:
    def mergeAdjacent(self, nums: List[int]) -> List[int]:
        result = []
        for num in nums:
            while result and result[-1] == num:
                num += result.pop()

            result.append(num)

        return result
