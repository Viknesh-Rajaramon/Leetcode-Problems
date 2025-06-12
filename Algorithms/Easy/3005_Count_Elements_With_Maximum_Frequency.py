from imports import *

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counts = Counter(nums)

        max_freq, total_freq = 0, 0
        for count in counts.values():
            if count > max_freq:
                max_freq = count
                total_freq = count
            elif count == max_freq:
                total_freq += count
        
        return total_freq
