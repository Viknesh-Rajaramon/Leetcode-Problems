from math import inf

class Solution:
    def maxProductPair(self, nums: list[int], target: int) -> list[int]:
        result, n, best, index = [-1, -1], len(nums), -inf, {}
        for i in range(n):
            if target - nums[i] in index:
                j = index[target - nums[i]]
                if nums[i] != nums[j] and nums[i] * nums[j] > best:
                    best = nums[i] * nums[j]
                    result = [i, j] if nums[i] > nums[j] else [j, i]
            
            index[nums[i]] = i

        return result
