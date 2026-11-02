class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        result, median = 0, nums[len(nums)//2]
        for num in nums:
            result += abs(num - median)

        return result
