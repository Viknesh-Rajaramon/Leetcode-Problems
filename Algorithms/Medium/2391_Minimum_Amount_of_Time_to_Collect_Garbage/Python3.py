from typing import List

class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        n = len(garbage)
        
        last_index = {"M": 0, "P": 0, "G": 0}
        for i in range(n-1, -1, -1):
            for c in ["M", "P", "G"]:
                if last_index[c] == 0 and c in garbage[i]:
                    last_index[c] = i
            
            if all(val != 0 for val in last_index.values()):
                break
        
        result = sum(garbage[0].count(c) for c in last_index.keys())
        for i in range(1, n):
            for c in last_index.keys():
                if i <= last_index[c]:
                    result += travel[i-1]
                
                result += garbage[i].count(c)
        
        return result
