from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {c: i for i, c in enumerate(s)}
        
        result = []
        start, end = 0, 0
        for i, c in enumerate(s):
            end = max(end, last[c])
            if end == i:
                result.append(end - start + 1)
                start = end + 1
            
        return result
