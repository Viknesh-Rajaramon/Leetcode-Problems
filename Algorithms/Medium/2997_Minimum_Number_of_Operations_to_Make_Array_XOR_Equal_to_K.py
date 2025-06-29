from imports import *

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        total_xor = k
        for num in nums:
            total_xor ^= num

        return bin(total_xor)[2 : ].count("1")
