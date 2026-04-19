from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        result, stack = 0, [0]
        for num in nums:
            while stack[-1] > num:
                stack.pop()
            
            if num > stack[-1]:
                result += 1
            
            stack.append(num)

        return result
