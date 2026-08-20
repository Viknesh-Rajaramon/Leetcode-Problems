from typing import List

class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        result[0], result[n-1] = nums[0], nums[1]
        idx, rev_idx = 0, n-1
        for i in range(2, n):
            if result[idx] > result[rev_idx]:
                idx += 1
                result[idx] = nums[i]
            else:
                rev_idx -= 1
                result[rev_idx] = nums[i]
        
        l, r = rev_idx, n-1
        while l < r:
            result[l], result[r] = result[r], result[l]
            l += 1
            r -= 1

        return result
