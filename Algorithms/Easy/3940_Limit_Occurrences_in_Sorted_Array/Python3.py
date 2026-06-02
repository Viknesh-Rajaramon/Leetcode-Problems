class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        i = 0
        for num in nums:
            if i < k or num != nums[i-k]:
                nums[i] = num
                i += 1
        
        return nums[ : i]
