from typing import List

class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        for layer in range(min(m, n)//2):
            r, c, nums = [], [], []
            for i in range(layer, m-1-layer):
                r.append(i)
                c.append(layer)
                nums.append(grid[i][layer])
            
            for j in range(layer, n-1-layer):
                r.append(m-1-layer)
                c.append(j)
                nums.append(grid[m-1-layer][j])
            
            for i in range(m-1-layer, layer, -1):
                r.append(i)
                c.append(n-1-layer)
                nums.append(grid[i][n-1-layer])
            
            for j in range(n-1-layer, layer, -1):
                r.append(layer)
                c.append(j)
                nums.append(grid[layer][j])
            
            total = len(nums)
            kk = k % total
            for i in range(total):
                idx = (i+total-kk) % total
                grid[r[i]][c[i]] = nums[idx]

        return grid
