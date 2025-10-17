from imports import *

class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        freq = [0] * value
        for num in nums:
            freq[num % value] += 1

        min_value_index = 0
        for i in range(1, value):
            if freq[i] < freq[min_value_index]:
                min_value_index = i
        
        return value * freq[min_value_index] + min_value_index
