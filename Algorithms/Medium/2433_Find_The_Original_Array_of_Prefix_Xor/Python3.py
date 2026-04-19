from typing import List

class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        arr = [pref[0]]
        for i in range(1, len(pref)):
            xor = pref[i-1] ^ pref[i]
            arr.append(xor)
        
        return arr
