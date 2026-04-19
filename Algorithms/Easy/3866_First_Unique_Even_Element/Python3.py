from collections import Counter

class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        freq = Counter(nums)
        for num, count in freq.items():
            if num % 2 == 0 and count == 1:
                return num
            
        return -1
