from imports import *

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        result = []
        
        arr1_count = Counter(arr1)
        for i in range(len(arr2)):
            result += [arr2[i]] * arr1_count[arr2[i]]
            arr1_count[arr2[i]] = 0
        
        for key, val in sorted(arr1_count.items()):
            if val == 0:
                continue
            
            result += [key] * val
        
        return result
