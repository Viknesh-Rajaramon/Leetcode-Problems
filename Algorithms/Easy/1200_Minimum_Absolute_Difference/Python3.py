from typing import List
from math import inf

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        diff = inf
        result = []
        for i in range(len(arr)-1):
            if arr[i+1] - arr[i] == diff:
                result.append([arr[i], arr[i+1]])
            elif arr[i+1] - arr[i] < diff:
                result = [[arr[i], arr[i+1]]]
                diff = arr[i+1] - arr[i]
                
        return result
