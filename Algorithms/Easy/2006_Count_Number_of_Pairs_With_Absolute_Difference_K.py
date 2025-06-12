from imports import *

class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        
        result = 0
        for num, count in counts.items():
            if num-k in counts:
                result += count * counts[num-k]
            
            if num+k in counts:
                result += count * counts[num+k]
        
        return result // 2
