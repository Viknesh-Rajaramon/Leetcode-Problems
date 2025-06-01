from imports import *

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        min_rolls = [-1] * (n**2 + 1)
        min_rolls[1] = 0

        queue = deque([1])
        while queue:
            x = queue.popleft()
            for i in range(1, 7):
                t = x + i
                if t > n*n:
                    break
                
                row = (t - 1) // n
                col = (t - 1) % n

                v = board[n-1-row][(n-1-col) if row % 2 else col]
                y = v if v > 0 else t

                if y == n*n:
                    return min_rolls[x] + 1
                
                if min_rolls[y] == -1:
                    min_rolls[y] = min_rolls[x] + 1
                    queue.append(y)

        return -1
