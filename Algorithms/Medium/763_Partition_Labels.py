from imports import *

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        first, last = {}, {}

        for i, c in enumerate(s):
            if c not in first:
                first[c] = i
            
            last[c] = i
        
        ans = []
        start = 0
        end = -1
        for c, pos in sorted(first.items(), key = lambda x: x[1]):
            if end == -1:
                end = last[c]
            elif pos < end:
                end = max(end, last[c])
            else:
                ans.append(end-start+1)
                start = pos
                end = last[c]
        
        if start != end+1:
            ans.append(end-start+1)
        
        return ans
