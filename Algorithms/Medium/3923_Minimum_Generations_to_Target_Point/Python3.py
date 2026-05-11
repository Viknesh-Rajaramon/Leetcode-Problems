from types import List
from itertools import combinations

class Solution:
    def minGenerations(self, points: List[List[int]], target: List[int]) -> int:
        seen, target = set(tuple(p) for p in points), tuple(target)
        if target in seen:
            return 0
        
        result = 0
        while True:
            new_states = set()
            for a, b in combinations(seen, 2):
                c = ((a[0]+b[0])//2, (a[1]+b[1])//2, (a[2]+b[2])//2)
                if c not in seen:
                    new_states.add(c)
                
            if not new_states:
                return -1
            
            result += 1
            if target in new_states:
                break
            
            seen |= new_states

        return result
