from imports import *

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        def dfs(i: int, j: int, index: int):
            if not (0 <= i < m and 0 <= j < n and index < len(word) and board[i][j] == word[index]):
                return False
            
            if index == len(word)-1:
                return True

            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                temp = board[i][j]
                board[i][j] = -1

                if dfs(i + di, j + dj, index + 1):
                    return True
                
                board[i][j] = temp
            
            return False

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        
        return False
