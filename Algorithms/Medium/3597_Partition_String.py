from imports import *

class Solution:
    def partitionString(self, s: str) -> List[str]:
        result = []
        seen = set()
        
        curr = ""
        for c in s:
            curr += c
            if curr not in seen:
                result.append(curr)
                seen.add(curr)
                curr = ""
        
        return result
