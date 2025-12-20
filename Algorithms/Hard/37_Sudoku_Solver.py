from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols, boxes, empties = [0] * 9, [0] * 9, [0] * 9, []
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    empties.append((i, j))
                else:
                    mask = 1 << (int(board[i][j]) - 1)
                    rows[i] |= mask
                    cols[j] |= mask
                    boxes[(i // 3) * 3 + (j // 3)] |= mask
        
        def backtrack(idx: int) -> bool:
            if idx == len(empties):
                return True
            
            i, j = empties[idx]
            bi = (i // 3) * 3 + (j // 3)
            used = rows[i] | cols[j] | boxes[bi]
            for d in range(9):
                m = 1 << d
                if not (used & m):
                    board[i][j] = str(d+1)
                    rows[i] |= m
                    cols[j] |= m
                    boxes[bi] |= m
                    if backtrack(idx + 1):
                        return True
                    
                    board[i][j] = "."
                    rows[i] &= ~m
                    cols[j] &= ~m
                    boxes[bi] &= ~m

            return False
        
        backtrack(0)
