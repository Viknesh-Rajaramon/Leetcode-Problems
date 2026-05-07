from bisect import bisect_left

class Solution:
    def maxFixedPoints(self, nums: list[int]) -> int:
        result, s = [], sorted([(i-num, num) for i, num in enumerate(nums) if i >= num])
        for _, num in s:
            idx = bisect_left(result, num)
            if idx == len(result):
                result.append(num)
            else:
                result[idx] = num
        
        return len(result)
