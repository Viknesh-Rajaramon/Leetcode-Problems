from typing import List
from math import log2
from heapq import heapify, heappop, heappush
        
class SparseTableOp:
    def __init__(self, arr: List[int], op):
        self.n = len(arr)
        self.k = int(log2(self.n)) + 1
        self.table = [[0] * self.k for _ in range(self.n)]
        self.op = op
            
        for i in range(self.n):
            self.table[i][0] = arr[i]
                
        for j in range(1, self.k):
            for i in range(self.n - (1 << j) + 1):
                self.table[i][j] = op(self.table[i][j-1], self.table[i + (1 << (j-1))][j-1])
            
    def query(self, left: int, right: int) -> int:
        k = int(log2(right - left + 1))
        return self.op(self.table[left][k], self.table[right - (1 << k) + 1][k])

class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n = len(nums)
        st_max, st_min = SparseTableOp(nums, max), SparseTableOp(nums, min)

        max_heap = []
        for i in range(n):
            max_heap.append((st_min.query(i, n-1) - st_max.query(i, n-1), i, n-1))
        
        heapify(max_heap)

        result = 0
        for _ in range(k):
            val, i, j = heappop(max_heap)
            result -= val
            if j - 1 >= i:
                heappush(max_heap, (st_min.query(i, j-1) - st_max.query(i, j-1), i, j-1))

        return result
