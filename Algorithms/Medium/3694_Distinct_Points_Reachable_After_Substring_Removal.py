class Solution:
    def distinctPoints(self, s: str, k: int) -> int:
        directions = {"U": (0, 1), "D": (0, -1), "L": (-1, 0), "R": (1, 0)}
        x, y, found = 0, 0, set([(0, 0)])
        for i in range(k, len(s)):
            dx, dy = directions[s[i]]
            x += dx
            y += dy
            dx, dy = directions[s[i - k]]
            x -= dx
            y -= dy
            found.add((x, y))
        
        return len(found)
