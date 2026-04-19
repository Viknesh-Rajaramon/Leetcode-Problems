from typing import List
from bisect import bisect_left

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low, high = 0, len(matrix)-1
        while low < high:
            mid = (low + high) // 2

            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target <= matrix[mid][-1]:
                low = mid
                break
            elif matrix[mid][0] > target:
                high = mid - 1
            else:
                low = mid + 1
        
        row_index = low
        col_index = bisect_left(matrix[row_index], target)

        if col_index == len(matrix[row_index]):
            return False
        
        if matrix[row_index][col_index] == target:
            return True
        
        return False
