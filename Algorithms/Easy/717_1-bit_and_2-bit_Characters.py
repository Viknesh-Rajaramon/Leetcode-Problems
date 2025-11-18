from imports import *

class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        n, i = len(bits)-1, 0
        while i < n:
            i += bits[i] + 1
        
        return i == n
