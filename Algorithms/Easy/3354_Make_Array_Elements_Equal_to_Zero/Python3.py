from typing import List

class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        result, left, right = 0, 0, sum(nums)
        for num in nums:
            if num == 0:
                if left == right:
                    result += 2
                elif abs(left - right) == 1:
                    result += 1
            else:
                left += num
                right -= num

        return result
