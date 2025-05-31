from imports import *

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        
        def backtrack(start: int, path: List[int], target: int) -> None:
            if target == 0:
                result.append(path)
                return
            
            for i in range(start, len(candidates)):
                if candidates[i] > target:
                    break
                
                backtrack(i, path + [candidates[i]], target - candidates[i])
        
        backtrack(0, [], target)
        return result
