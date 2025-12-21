from typing import List

class Solution:
    def maxBalancedSubarray(self, nums: List[int]) -> int:
        result, odd_even, xor, visited = 0, 0, 0, {(0, 0): 0}
        for i, num in enumerate(nums, start = 1):
            odd_even += 1 if num%2 else -1
            xor ^= num
            if (xor, odd_even) in visited:
                result = max(result, i - visited[(xor, odd_even)])
            else:
                visited[(xor, odd_even)] = i

        return result
