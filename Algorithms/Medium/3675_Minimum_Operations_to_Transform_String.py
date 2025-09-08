from imports import *

class Solution:
    def minOperations(self, s: str) -> int:
        for i, c in enumerate(string.ascii_lowercase[1 : ]):
            if s.count(c) > 0:
                return 25 - i
        
        return 0
