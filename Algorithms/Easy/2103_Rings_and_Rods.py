from imports import *

class Solution:
    def countPoints(self, rings: str) -> int:
        rings_map = defaultdict(set)
        for i in range(0, len(rings), 2):
            rings_map[rings[i+1]].add(rings[i])
        
        return sum(1 for r in rings_map.values() if len(r) == 3)
