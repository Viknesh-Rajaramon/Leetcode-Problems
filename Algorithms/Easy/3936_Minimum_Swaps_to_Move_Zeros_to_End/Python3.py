class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        result, left, right = 0, 0, len(nums)-1
        while left < right:
            while right >= 0 and nums[right] == 0:
                right -= 1
            
            if right < 0 or right < left:
                break

            if nums[left] == 0:
                result += 1
                right -= 1
                
            left += 1

        return result
