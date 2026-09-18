class Solution:
    def minInitialStrength(self, monsters: list[int], boosts: list[list[int]]) -> int:
        n = len(monsters)
        diff, bonus = [0] * (n+1), [0] * n
        for l, r, v in boosts:
            diff[l] += v
            diff[r+1] -= v
        
        bonus[0] = diff[0]
        for i in range(1, n):
            bonus[i] = bonus[i-1] + diff[i]
        
        result = 0
        for i in range(n-1, -1, -1):
            if result == 0:
                result = max(0, monsters[i] - bonus[i])
            else:
                result += monsters[i]

        return result
