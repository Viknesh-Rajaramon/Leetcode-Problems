from imports import *

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)

        result = []
        def backtrack(index: int, nums: List[int], target: int):
            if target == 0:
                result.append(nums.copy())
                return
            
            if target < 0:
                return
            
            for i in range(index, n):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                
                if candidates[i] > target:
                    break
                
                backtrack(i+1, nums + [candidates[i]], target - candidates[i])

        backtrack(0, [], target)
        return result
