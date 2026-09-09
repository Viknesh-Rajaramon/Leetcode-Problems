class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        mid = len(nums)//2
        for i in range(len(nums)):
            if i == mid:
                continue

            if nums[i] == nums[mid]:
                return False

        return True
