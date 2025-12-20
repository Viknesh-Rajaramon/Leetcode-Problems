from typing import List

class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        last = len(s) % k
        if last:
            s += fill * (k - last)
        
        return [s[i : i+k] for i in range(0, len(s), k)]
