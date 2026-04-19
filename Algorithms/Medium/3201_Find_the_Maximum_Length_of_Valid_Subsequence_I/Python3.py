from typing import List

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        odd_p, odd_q, even_p, even_q = 0, 0, 0, 0
        for num in nums:
            if num % 2:
                odd_p += 1
                odd_q = 1 + even_q
            else:
                even_p += 1
                even_q = 1 + odd_q

        return max(odd_p, odd_q, even_p, even_q)
