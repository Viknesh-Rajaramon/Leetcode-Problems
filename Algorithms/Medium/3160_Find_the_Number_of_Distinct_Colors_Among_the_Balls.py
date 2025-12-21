from typing import List

class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ball_map = {}
        color_map = {}

        ans = []

        n = len(queries)
        for i in range(n):
            ball = queries[i][0]
            new_color = queries[i][1]

            old_color = ball_map.get(ball, 0)
            if old_color != 0:
                color_map[old_color] -= 1
            
                if color_map[old_color] == 0:
                    del color_map[old_color]
            
            if new_color not in color_map:
                color_map[new_color] = 0
            
            ball_map[ball] = new_color
            color_map[new_color] = color_map.get(new_color, 0) + 1
            ans.append(len(color_map))
        
        return ans
