from typing import List

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        paths_map = {}
        for src, dst in paths:
            paths_map[src] = dst
        
        final_dst = paths[0][1]
        while final_dst in paths_map:
            final_dst = paths_map[final_dst]
        
        return final_dst
