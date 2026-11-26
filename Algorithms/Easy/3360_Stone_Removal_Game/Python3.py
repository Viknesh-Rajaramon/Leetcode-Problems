class Solution:
    def canAliceWin(self, n: int) -> bool:
        result, take = False, 10
        while n >= take:
            n -= take
            take -= 1
            result = not result
        
        return result
