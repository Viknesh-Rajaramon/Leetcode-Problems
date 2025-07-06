class Solution:
    def minMoves(self, sx: int, sy: int, tx: int, ty: int) -> int:
        result = 0

        x, y = tx, ty
        while x > sx or y > sy:
            result += 1

            if x < y or x == y and sx > sy:
                x, y, sx, sy = y, x, sy, sx

            if x >= 2*y:
                if x % 2:
                    return -1

                x //= 2
            else:
                x -= y

        return result if x == sx and y == sy else -1
