class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        empty = numBottles
        result = numBottles
        while empty >= numExchange:
            result += 1
            empty -= numExchange - 1
            numExchange += 1

        return result
