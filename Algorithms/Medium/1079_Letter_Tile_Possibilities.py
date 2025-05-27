from imports import *

class Solution:
    def permutationsCount(self, tiles_map: dict, length: int) -> int:
        count = 0
        for c in tiles_map.keys():
            if tiles_map[c] == 0:
                continue

            tiles_map[c] -= 1
            count += 1 + self.permutationsCount(tiles_map, length-1)
            tiles_map[c] += 1
        
        return count

    def numTilePossibilities(self, tiles: str) -> int:
        tiles_count = defaultdict(int)

        for c in tiles:
            tiles_count[c] += 1
        
        return self.permutationsCount(tiles_count, len(tiles))
