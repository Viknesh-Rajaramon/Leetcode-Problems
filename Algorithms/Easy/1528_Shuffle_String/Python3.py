from typing import List

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        result = [""] * len(indices)
        for i, c in zip(indices, s):
            result[i] = c
        
        return "".join(result)
