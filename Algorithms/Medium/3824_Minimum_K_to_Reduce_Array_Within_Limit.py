from typing import List

class Solution:
    def minimumK(self, nums: List[int]) -> int:
        low, high = 1, sum(nums)
        while low < high:
            mid = (low + high) // 2
            if sum((num + mid - 1) // mid for num in nums) <= mid**2:
                high = mid
            else:
                low = mid + 1

        return low
