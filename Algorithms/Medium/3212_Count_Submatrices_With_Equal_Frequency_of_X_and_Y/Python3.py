from typing import List

class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        result, m, n = 0, len(grid), len(grid[0])
        dp_1, dp_2 = [0] * n, [0] * n
        for i in range(m):
            pre_1, pre_2 = 0, 0
            for j in range(n):
                if grid[i][j] == ".":
                    pass
                elif grid[i][j] == "X":
                    dp_1[j] += 1
                    dp_2[j] += 1
                else:
                    dp_1[j] -= 1
            
                pre_1 += dp_1[j]
                pre_2 += dp_2[j]
                if pre_1 == 0 and pre_2 > 0:
                    result += 1
        
        return result
