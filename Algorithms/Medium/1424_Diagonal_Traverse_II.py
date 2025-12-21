from typing import List

class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        tuples = []
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                tuples.append((i+j, -i, nums[i][j]))
        
        tuples.sort()
        return [val for _, _, val in tuples]
