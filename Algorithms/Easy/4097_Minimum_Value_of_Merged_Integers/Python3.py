from math import inf

class Solution:
    def minMergedInteger(self, nums: list[int]) -> int:        
        result = inf
        for i in range(0, len(nums), 2):
            result = min(result, int(str(nums[i]) + str(nums[i+1])))

        return result
