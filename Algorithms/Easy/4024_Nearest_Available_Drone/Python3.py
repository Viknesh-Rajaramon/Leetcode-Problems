from math import inf

class Solution:
    def nearestDrone(self, drones: list[list[int]], target: list[int]) -> int:
        result, min_dist = -1, inf
        for i in range(len(drones)):
            dist = abs(drones[i][0] - target[0]) + abs(drones[i][1] - target[1])
            if dist <= drones[i][2] and dist < min_dist:
                result, min_dist = i, dist

        return result
