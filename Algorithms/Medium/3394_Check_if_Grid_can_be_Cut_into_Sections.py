from imports import *

class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        def is_possible(dim) -> bool:
            rectangles.sort(key = lambda x: x[dim])
            sections = 0
            max_end = 0
            for r in rectangles:
                if max_end <= r[dim]:
                    sections += 1
                    if sections == 3:
                        return True
                
                if max_end < r[dim+2]:
                    max_end = r[dim+2]
            
            return False

        return is_possible(0) or is_possible(1)
