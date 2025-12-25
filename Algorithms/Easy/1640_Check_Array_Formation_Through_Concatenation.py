from typing import List

class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        pieces_map, i = {p[0]: p for p in pieces}, 0
        while i < len(arr):
            first = arr[i]
            if first in pieces_map:
                for p in pieces_map[first]:
                    if arr[i] != p:
                        return False
                    i += 1
            else:
                return False
            
        return True
