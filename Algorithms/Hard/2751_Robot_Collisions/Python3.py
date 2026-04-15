from typing import List

class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        stack = []
        for i in sorted(range(len(positions)), key = lambda x: positions[x]):
            if directions[i] == "R":
                stack.append(i)
                continue
            
            while stack and healths[i] > 0:
                if healths[stack[-1]] > healths[i]:
                    healths[stack[-1]] -= 1
                    healths[i] = 0
                elif healths[stack[-1]] < healths[i]:
                    healths[stack.pop()] = 0
                    healths[i] -= 1
                else:
                    healths[stack.pop()] = 0
                    healths[i] = 0

        return [health for health in healths if health > 0]
