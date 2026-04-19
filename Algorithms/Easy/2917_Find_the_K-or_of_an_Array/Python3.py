from typing import List

class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        result = 0
        for bit in range(32):
            count = 0
            y = 2**bit
            for x in nums:
                if y & x:
                    count += 1
                    if count == k:
                        result += y

        return result
