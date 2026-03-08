from typing import List
from heapq import heapify, heappop

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n, nums_int = len(nums[0]), [int(num, 2) for num in nums]
        heapify(nums_int)
        for i in range(2**n):
            if len(nums_int) == 0 or i != heappop(nums_int):
                break
            
        result = []
        for _ in range(n):
            result.append(i % 2)
            i = i // 2
            
        return "".join(str(i) for i in result[::-1])
