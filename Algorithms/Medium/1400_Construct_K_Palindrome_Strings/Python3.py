from collections import Counter

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        
        if sum(val%2 for val in Counter(s).values()) > k:
            return False
        
        return True
