from typing import List
from heapq import heappop, heappushpop, heapify

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        count = len(stones)-1
        stones = list(map(lambda x: x * -1, stones))
        heapify(stones)

        x = -heappop(stones)
        while count > 0:
            y = -heappop(stones)
            x = -heappushpop(stones, y-x)
            count -= 1

        return x
