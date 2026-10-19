class Solution:
    def minDeletions(self, nums: list[int]) -> int:
        result = 0
        for i in range(len(nums)-1):
            if nums[i] ^ nums[i+1] == 0:
                result += 1

        return result
