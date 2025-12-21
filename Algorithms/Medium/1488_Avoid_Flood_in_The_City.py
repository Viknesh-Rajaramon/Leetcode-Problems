from typing import List
from collections import deque

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        last, queue = {}, deque()
        
        result = []
        for i, lake in enumerate(rains):
            if lake:
                if lake in last:
                    for j in queue:
                        if j > last[lake]:
                            result[j] = lake
                            queue.remove(j)
                            break
                    else:
                        return []

                result.append(-1)
                last[lake] = i
            else:
                result.append(1)
                queue.append(i)
        
        return result
