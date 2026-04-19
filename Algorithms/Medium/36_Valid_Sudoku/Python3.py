from typing import List

digits = [str(i) for i in range(1, 10)]

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def check_smaller_grid(row: int, col: int) -> bool:
            nums = set()
            for i in range(row, row + 3):
                for j in range(col, col + 3):
                    if board[i][j] in digits:
                        if board[i][j] in nums:
                            return False
                        else:
                            nums.add(board[i][j])
            
            return True
        
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                if not check_smaller_grid(row, col):
                    return False
        
        for row in range(9):
            visited = set()
            for col in range(9):
                if board[row][col] in digits:
                    if board[row][col] in visited:
                        return False
                    else:
                        visited.add(board[row][col])
        
        for col in range(9):
            visited = set()
            for row in range(9):
                if board[row][col] in digits:
                    if board[row][col] in visited:
                        return False
                    else:
                        visited.add(board[row][col])

        return True