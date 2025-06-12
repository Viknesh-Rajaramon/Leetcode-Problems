from imports import *

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = Counter(arr)
        s = set()
        for count in counts.values():
            if count in s:
                return False
            
            s.add(count)

        return True
