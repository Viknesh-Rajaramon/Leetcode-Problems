from typing import List
from collections import defaultdict

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        n = len(time)
        hash_map = defaultdict(int)
        
        for i in range(n):
            hash_map[time[i] % 60] += 1
        
        result = 0
        for i in range(n):
            new_time = (60 - (time[i] % 60)) % 60
            if new_time not in hash_map:
                continue
            
            if new_time == time[i] % 60:
                result += hash_map[new_time] - 1
            else:
                result += hash_map[new_time]
        
        return result // 2
