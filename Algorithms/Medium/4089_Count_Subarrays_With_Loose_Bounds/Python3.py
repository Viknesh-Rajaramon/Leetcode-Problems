class Solution:
    def countSubarrays(self, nums: list[int], minK: int, maxK: int) -> int:
        result, l = 0, 0
        for r in range(len(nums)):
            if nums[r] < minK or nums[r] > maxK:
                l = r+1
            else:
                result += r-l+1

        return result
