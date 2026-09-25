class Solution:
    def findDisappearedNumbers(self, nums: list[int], lower: int, upper: int) -> list[list[int]]:
        result, nums, start = [], set(nums), lower
        for end in range(lower, upper+1):
            if end in nums:
                if start != end:
                    result.append([start, end-1])
                
                start = end+1
            elif end == upper:
                result.append([start, end])

        return result
