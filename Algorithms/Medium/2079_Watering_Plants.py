from imports import *

class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        result = 0
        curr_cap = capacity
        for i in range(len(plants)):
            if curr_cap >= plants[i]:
                curr_cap -= plants[i]
                result += 1
            else:
                result += 2*i + 1
                curr_cap = capacity - plants[i]

        return result
