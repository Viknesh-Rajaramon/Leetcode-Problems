from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        pos = n-1

        i, j = 0, n-1
        while i <= j:
            if abs(nums[i]) > abs(nums[j]):
                result[pos] = nums[i] * nums[i]
                i += 1
            else:
                result[pos] = nums[j] * nums[j]
                j -= 1

            pos -= 1
        
        return result
