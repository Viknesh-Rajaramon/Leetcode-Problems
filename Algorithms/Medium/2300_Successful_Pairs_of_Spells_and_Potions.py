from imports import *

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        m = len(potions)

        result = []
        for spell in spells:
            min_strength = ceil(success / spell)
            if min_strength > potions[-1]:
                result.append(0)
                continue

            idx = bisect_left(potions, min_strength)
            result.append(m-idx)
        
        return result
