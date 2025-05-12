class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        x_z = abs(x-z)
        y_z = abs(y-z)

        if x_z == y_z:
            return 0
        elif x_z < y_z:
            return 1

        return 2
