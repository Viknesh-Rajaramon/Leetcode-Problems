from typing import List

class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        def solve(firstStart: List[int], firstDur: List[int], secondStart: List[int], secondDur: List[int]) -> int:
            end = min(s + d for s, d in zip(firstStart, firstDur))
            return min(max(s, end) + d for s, d in zip(secondStart, secondDur))
        
        return min(
            solve(landStartTime, landDuration, waterStartTime, waterDuration),
            solve(waterStartTime, waterDuration, landStartTime, landDuration)
        )
