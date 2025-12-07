from imports import *

class Solution:
    def minInversionCount(self, nums: List[int], k: int) -> int:
        n, sl, count, result = len(nums), [], 0, inf
        for i in range(n):
            if i - k >= 0:
                count -= bisect_left(sl, (nums[i-k], 0))
                pos = bisect_left(sl, (nums[i-k], i-k))
                if pos < len(sl) and sl[pos] == (nums[i-k], i-k):
                    sl.pop(pos)
            
            count += len(sl) - bisect_right(sl, (nums[i], inf))
            sl.insert(bisect_right(sl, (nums[i], i)), (nums[i], i))

            if i >= k-1:
                result = min(result, count)

        return result
