from imports import *

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n, result = len(nums), []
        def backtrack(comb: List[int], counter: Counter):
            if len(comb) == n:
                result.append(comb.copy())
                return
            
            for num in counter:
                if counter[num] > 0:
                    comb.append(num)
                    counter[num] -= 1
                    backtrack(comb, counter)
                    comb.pop()
                    counter[num] += 1

        backtrack([], Counter(nums))
        return result
