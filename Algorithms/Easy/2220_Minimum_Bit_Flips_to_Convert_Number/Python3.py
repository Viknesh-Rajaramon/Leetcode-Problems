class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        result = start ^ goal
        count = 0
        while result > 0:
            count += result % 2
            result = result // 2
        
        return count
