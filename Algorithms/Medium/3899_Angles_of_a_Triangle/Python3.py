from math import degrees, acos

class Solution:
    def internalAngles(self, sides: list[int]) -> list[float]:
        sides.sort()
        if sides[0] + sides[1] <= sides[2]:
            return []

        a, b, c = sides
        A = degrees(acos((b**2+c**2-a**2)/(2*b*c)))
        B = degrees(acos((a**2+c**2-b**2)/(2*a*c)))
        C = degrees(acos((a**2+b**2-c**2)/(2*a*b)))
        return sorted([A, B, C])
