class Solution:
    def maxDistance(self, moves: str) -> int:
        x, y, extra = 0, 0, 0
        for c in moves:
            if c == 'R':
                x += 1
            elif c == 'L':
                x -= 1
            elif c == 'U':
                y += 1
            elif c == 'D':
                y -= 1
            else:
                extra += 1

        return abs(x) + abs(y) + extra
