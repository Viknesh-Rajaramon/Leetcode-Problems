class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        result = x ^ y
        count = 0
        while result > 0:
            count += result % 2
            result = result // 2
        
        return count
