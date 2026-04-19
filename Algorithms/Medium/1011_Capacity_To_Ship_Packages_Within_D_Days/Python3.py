from typing import List

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def checkWeight(ship_capacity: int) -> bool:
            days_needed = 0
            curr_weight = 0
            
            for w in weights:
                if curr_weight + w > ship_capacity:
                    days_needed += 1
                    curr_weight = 0
                
                curr_weight += w

            if curr_weight > 0:
                days_needed += 1
            
            return days_needed <= days
        
        low, high = max(weights), sum(weights)
        while low <= high:
            mid = (low + high) // 2

            if checkWeight(mid):
                high = mid - 1
            else:
                low = mid + 1
        
        return low
