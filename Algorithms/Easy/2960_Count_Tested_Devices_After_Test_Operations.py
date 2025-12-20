from typing import List

class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        result = 0
        for battery in batteryPercentages:
            if battery - result > 0:
                result += 1
        
        return result
