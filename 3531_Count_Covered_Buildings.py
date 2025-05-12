from imports import *

class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        hash_x, hash_y = defaultdict(SortedList), defaultdict(SortedList)

        for i, b in enumerate(buildings):
            hash_x[b[0]].add((b[1], i))
            hash_y[b[1]].add((b[0], i))
        
        set_x = set()
        for x, x_list in hash_x.items():
            set_x.update([index for _, index in x_list[1:-1]])
        
        set_y = set()
        for y, y_list in hash_y.items():
            set_y.update([index for _, index in y_list[1:-1]])
        
        return len(set_x.intersection(set_y))
