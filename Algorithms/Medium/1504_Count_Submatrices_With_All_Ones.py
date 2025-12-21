from typing import List

class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        def count_rows(heights: List[int]) -> int:
            stack, sub_matrices = [], [0] * n
            for i in range(n):
                while stack and heights[stack[-1]] >= heights[i]:
                    stack.pop()
                
                if stack:
                    l = stack[-1]
                    sub_matrices[i] = sub_matrices[l] + heights[i] * (i-l)
                else:
                    sub_matrices[i] = heights[i] * (i+1)
        
                stack.append(i)
            
            return sum(sub_matrices)

        result, heights = 0, [0] * n
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    heights[j] += 1
                else:
                    heights[j] = 0
                    
            result += count_rows(heights)
        
        return result
