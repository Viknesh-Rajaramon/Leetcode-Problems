class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        result = 0
        
        north = south = east = west = 0
        for c in s:
            if c == "N":
                north += 1
            elif c == "S":
                south += 1
            elif c == "E":
                east += 1
            elif c == "W":
                west += 1
            
            ns_change = min(north, south, k)
            ew_change = min(east, west, k - ns_change)
            dis = abs(north - south) + abs(east - west) + 2 * (ns_change + ew_change)
            result = max(result, dis)
        
        return result
