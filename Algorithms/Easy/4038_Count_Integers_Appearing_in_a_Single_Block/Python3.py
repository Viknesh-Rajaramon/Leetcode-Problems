class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        first, last, freq = {}, {}, {}
        for i, num in enumerate(nums):
            if num not in first:
                first[num] = i
                freq[num] = 0
            
            last[num] = i
            freq[num] += 1
        
        result = 0
        for num in freq:
            if last[num] - first[num] + 1 == freq[num]:
                result += 1

        return result
