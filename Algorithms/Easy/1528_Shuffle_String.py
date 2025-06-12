from imports import *

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        n = len(s)
        result = [""] * n
        for i in range(n):
            result[indices[i]] = s[i]
        
        return "".join(result)
