from imports import *

class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        user_uam = defaultdict(set)
        for id_, time in logs:
            user_uam[id_].add(time)
        
        result = [0] * k
        for times in user_uam.values():
            result[len(times)-1] += 1

        return result
