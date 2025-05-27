from imports import *

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        edge_1, edge_2 = edges[0], edges[1]
        if edge_1[0] == edge_2[0] or edge_1[0] == edge_2[1]:
            return edge_1[0]

        return edge_1[1]
