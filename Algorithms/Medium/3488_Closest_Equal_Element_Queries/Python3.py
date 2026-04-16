from typing import List
from collections import defaultdict

class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        def binary_search(arr: List[int], x: int) -> int:
            low, high = 0, len(arr)-1
            while low <= high:
                mid = (low+high) // 2
                if arr[mid] == x:
                    return mid
                elif arr[mid] < x:
                    low = mid+1
                else:
                    high = mid-1

            return -1
        
        n, hash_map = len(nums), defaultdict(list)
        for i in range(n):
            hash_map[nums[i]].append(i)

        result = []
        for q in queries:
            indices = hash_map[nums[q]]
            if len(indices) == 1:
                result.append(-1)
                continue
            
            i = binary_search(indices, q)
            if i == len(indices)-1:
                i = min(indices[i] - indices[-2], n + indices[0] - indices[i])
            elif i == 0:
                i = min(indices[1] - indices[i], n + indices[i] - indices[-1])
            else:
                i = min(indices[i+1] - indices[i], indices[i] - indices[i-1])
                
            result.append(i)
        
        return result
