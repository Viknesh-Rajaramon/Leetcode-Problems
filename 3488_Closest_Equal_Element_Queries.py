from imports import *

class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        def binary_search(arr: List[int], x: int) -> int:
            l, r = 0, len(arr)-1
            while l <= r:
                m = (l+r) // 2
                if arr[m] == x:
                    return m
                elif arr[m] < x:
                    l = m+1
                else:
                    r = m-1

            return -1
        
        n = len(nums)
        hash_map = defaultdict(list)

        for i in range(n):
            hash_map[nums[i]].append(i)

        ans = []
        for q in queries:
            indices = hash_map[nums[q]]
            if len(indices) == 1:
                ans.append(-1)
                continue
            
            index = binary_search(indices, q)
            if index == len(indices)-1:
                index = min(indices[index] - indices[-2], n+indices[0] - indices[index])
            elif index == 0:
                index = min(indices[1] - indices[index], n+indices[index] - indices[-1])
            else:
                index = min(indices[index+1] - indices[index], indices[index] - indices[index-1])
                
            ans.append(index)
        
        return ans
