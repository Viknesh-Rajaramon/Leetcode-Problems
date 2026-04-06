from typing import List

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        result, obs, x, y, dx, dy = 0, set(map(tuple, obstacles)), 0, 0, 0, 1
        for c in commands:
            if c < 0:
                dx, dy = (dy, -dx) if c == -1 else (-dy, dx)
                continue
            
            for _ in range(c):
                if (x+dx, y+dy) in obs:
                    break
                
                x, y = x+dx, y+dy
            
            result = max(result, x**2 + y**2)

        return result
