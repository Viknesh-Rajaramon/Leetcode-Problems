from typing import List

class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        grid = [[""] * 3 for _ in range(3)]
        char_map = {"x": "A", "o": "B"}
        
        for i in range(len(moves)):
            row, col = moves[i]
            if i % 2 == 0:
                grid[row][col] = "x"
            else:
                grid[row][col] = "o"
        
        def check_diagnols():
            char = grid[0][0]
            if char != "" and grid[1][1] == char and grid[2][2] == char:
                return char_map[char]
            
            char = grid[0][2]
            if char != "" and grid[1][1] == char and grid[2][0] == char:
                return char_map[char]
                
            return ""
        
        def check_rows():
            for row in range(3):
                char = grid[row][0]
                if char == "":
                    continue
                    
                if grid[row][1] == char and grid[row][2] == char:
                    return char_map[char]
                
            return ""
        
        def check_cols():
            for col in range(3):
                char = grid[0][col]
                if char == "":
                    continue
                    
                if grid[1][col] == char and grid[2][col] == char:
                    return char_map[char]
                
            return ""
        
        ans = ""
        ans = check_diagnols()
        if ans != "":
            return ans
        
        ans = check_rows()
        if ans != "":
            return ans
        
        ans = check_cols()
        if ans != "":
            return ans
        
        return "Draw" if len(moves) == 9 else "Pending"
