class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        empty = numBottles
        result = numBottles
        while empty >= numExchange:
            result += empty // numExchange
            empty = (empty % numExchange) + (empty // numExchange)

        return result
