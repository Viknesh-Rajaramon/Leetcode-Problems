from typing import List
from collections import defaultdict

class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        hash_map = defaultdict(int)
        for i in range(len(y)):
            hash_map[x[i]] = max(hash_map[x[i]], y[i])
        
        if len(hash_map) < 3:
            return -1
        
        max_val = [0, 0, 0]
        for val in hash_map.values():
            if max_val[0] <= val:
                max_val[2] = max_val[1]
                max_val[1] = max_val[0]
                max_val[0] = val
            elif max_val[1] <= val < max_val[0]:
                max_val[2] = max_val[1]
                max_val[1] = val
            elif max_val[2] <= val < max_val[1]:
                max_val[2] = val
            
        return sum(max_val)
