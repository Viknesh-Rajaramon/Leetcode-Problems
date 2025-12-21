from typing import List

class Solution:
    def calculateScore(self, instructions: List[str], values: List[int]) -> int:
        n = len(instructions)
        visited = set()
        score = 0

        i = 0
        while 0 <= i < n:
            if i in visited:
                break
            
            visited.add(i)
            if instructions[i] == "jump":
                i += values[i]
            elif instructions[i] == "add":
                score += values[i]
                i += 1
        
        return score
