from typing import List
from collections import defaultdict
from sortedcontainers import SortedList

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        diagonals = defaultdict(SortedList)

        for i in range(m):
            for j in range(n):
                diagonals[i-j].add(mat[i][j])
        
        track = defaultdict(int)
        for i in range(m):
            for j in range(n):
                diff = i-j
                mat[i][j] = diagonals[diff][track[diff]]
                track[diff] += 1
        
        return mat
