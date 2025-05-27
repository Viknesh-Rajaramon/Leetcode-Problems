from imports import *

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        counts = Counter(answers)

        result = 0
        for ans, count in counts.items():
            result = result + ceil(count / (ans + 1)) * (ans + 1)
        
        return result
