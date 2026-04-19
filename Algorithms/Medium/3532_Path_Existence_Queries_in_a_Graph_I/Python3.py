from typing import List

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        s = [-1] * n
        s[0] = 0

        for i in range(1, n):
            if nums[i] - nums[i-1] <= maxDiff:
                s[i] = s[i-1]
            else:
                s[i] = s[i-1] + 1
        
        result = []
        for u, v in queries:
            result.append(s[u] == s[v])
        
        return result
