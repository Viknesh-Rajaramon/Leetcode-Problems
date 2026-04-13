from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def area(heights: List[int]) -> int:
            max_area, n, stack = 0, len(heights), []
            for i in range(n+1):
                h = 0 if i == n else heights[i]
                while stack and h < heights[stack[-1]]:
                    height, width = heights[stack.pop()], i if not stack else i-stack[-1]-1
                    max_area = max(max_area, height*width)

                stack.append(i)

            return max_area

        row, col = len(matrix), len(matrix[0])
        result, hist = 0, [0] * col
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == "1":
                    hist[j] += 1
                else:
                    hist[j] = 0
            
            result = max(result, area(hist))
        
        return result
