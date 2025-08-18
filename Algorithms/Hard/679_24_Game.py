from imports import *

class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        error = 1e-6
        def dfs(nums: List[float]):
            if len(nums) == 1:
                return abs(nums[0] - 24) < error
            
            n = len(nums)
            for i in range(n):
                num1 = nums[i]
                for j in range(i+1, n):
                    num2 = nums[j]
                    next_nums = [nums[k] for k in range(n) if k != i and k != j]
                    for val in (num1+num2, num1-num2, num2-num1, num1*num2):
                        if dfs(next_nums + [val]):
                            return True
                    
                    if abs(num2) > error and dfs(next_nums + [num1/num2]):
                        return True
                    
                    if abs(num1) > error and dfs(next_nums + [num2/num1]):
                        return True
            
            return False
        
        return dfs(list(map(float, cards)))
