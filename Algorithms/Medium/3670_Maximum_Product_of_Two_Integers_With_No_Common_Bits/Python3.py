from typing import List

class Node:
    def __init__(self):
        self.l = None
        self.r = None
        self.v = None

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        root = Node()
        def insert(n, i, curr):
            for i in range(22, -1, -1):
                if (n >> i) & 1:
                    if not curr.r:
                        curr.r = Node()

                    curr = curr.r
                else:
                    if not curr.l:
                        curr.l = Node()

                    curr = curr.l

            curr.v = n

        mem = {}
        def find(n, b, curr):
            k = ((n & ((1 << (b + 1)) - 1)), b, id(curr))
            if k in mem:
                return mem[k]
            
            if curr.v is not None:
                mem[k] = curr.v
                return curr.v
            
            if (n >> b) & 1:
                if curr.l is None:
                    mem[k] = 0
                    return 0

                mem[k] = find(n, b - 1, curr.l)
                return mem[k]

            if curr.r is not None:
                mem[k] = find(n, b - 1, curr.r)
                if mem[k]: return mem[k]
            
            if curr.l is not None:
                mem[k] = find(n, b - 1, curr.l)
                if mem[k]: return mem[k]

            mem[k] = 0
            return 0

        for n in nums:
            insert(n, 22, root)

        best = 0
        for n in nums:
            best = max(best, n * find(n, 22, root))

        return best
