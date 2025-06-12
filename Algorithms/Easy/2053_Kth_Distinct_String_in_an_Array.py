from imports import *

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        counts = Counter(arr)

        for word, count in counts.items():
            if count == 1:
                k -= 1
                if k == 0:
                    return word
        
        return ""
