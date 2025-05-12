from imports import *

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums_count = [0 for _ in range(n-2)]
        for i in range(n):
            nums_count[nums[i]] += 1
        
        answer = []
        for i in range(n-2):
            if nums_count[i] == 2:
                answer.append(i)
        
        return answer
