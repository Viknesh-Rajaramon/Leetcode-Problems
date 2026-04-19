from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_num, length, max_length = max(nums), 0, 0
        for num in nums:
            if num == max_num:
                length += 1
            else:
                if length > max_length:
                    max_length = length
                
                length = 0

        return max_length if max_length > length else length
