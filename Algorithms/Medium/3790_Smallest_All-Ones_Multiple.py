class Solution:
    def minAllOneMultiple(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0:
            return -1

        remainder, seen = 0, set()
        for l in range(1, k+1):
            remainder = (remainder*10 + 1) % k
            if remainder == 0:
                return l

            if remainder in seen:
                return -1

            seen.add(remainder)

        return -1
