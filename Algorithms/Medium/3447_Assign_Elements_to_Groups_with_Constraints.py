from imports import *

class Solution:
    def assignElements(self, groups: List[int], elements: List[int]) -> List[int]:
        n = len(groups)
        max_group = max(groups)

        sieve = {}

        default_index = -1

        for i, ele in enumerate(elements):
            if ele == 1:
                default_index = i
                break
            
            if ele in sieve:
                continue
            
            for val in range(ele, max_group+1, ele):
                if val not in sieve:
                    sieve[val] = i
            
        result = []
        for i in range(n):
            chosen_index = sieve.get(groups[i], default_index)
            result.append(chosen_index)
        
        return result
