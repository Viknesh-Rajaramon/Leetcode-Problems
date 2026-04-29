from typing import List

class Solution:
    def maximumScore(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n == 1:
            return 0
        
        dp_0, dp_1 = [0] * (n+1), [0] * (n+1)
        for j in range(1, n):
            new_dp_0, new_dp_1 = [0] * (n+1), [0] * (n+1)
            for i in range(n+1):
                prev_col_val, curr_col_val = 0, sum(grid[p][j] for p in range(i))
                for k in range(n+1):
                    if k > 0 and k <= i:
                        curr_col_val -= grid[k-1][j]
                    
                    if k > i:
                        prev_col_val += grid[k-1][j-1]
                    
                    new_dp_1[k] = max(new_dp_1[k], dp_0[i], prev_col_val+dp_1[i])
                    new_dp_0[k] = max(new_dp_0[k], curr_col_val+dp_0[i], curr_col_val+prev_col_val+dp_1[i])
            
            dp_0, dp_1 = new_dp_0, new_dp_1

        return max(dp_0)
