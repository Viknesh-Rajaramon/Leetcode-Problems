from imports import *

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        def convertNumToString(num: int, length: int) -> str:
            digits = []
            for _ in range(length):
                digits.append(num % 2)
                num = num // 2
            
            return "".join(str(i) for i in digits[::-1])

        nums_int = [int(num, 2) for num in nums]
        heapify(nums_int)
        
        n = len(nums[0])
        i = 0

        for i in range(2**n):
            if len(nums_int) == 0 or i != heappop(nums_int):
                break
            
        return convertNumToString(i, n)
