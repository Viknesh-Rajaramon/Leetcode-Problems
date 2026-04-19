from typing import List

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix_xor = [0]
        for num in arr:
            prefix_xor.append(prefix_xor[-1] ^ num)
        
        result = []
        for l, r in queries:
            result.append(prefix_xor[r+1] ^ prefix_xor[l])
        
        return result
