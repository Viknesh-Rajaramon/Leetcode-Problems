from typing import List
from collections import deque

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n, queue, visited = len(arr), deque([start]), set([start])
        while queue:
            idx = queue.popleft()
            if arr[idx] == 0:
                return True
            
            left = idx-arr[idx]
            if left >= 0 and left not in visited:
                queue.append(left)
                visited.add(left)
            
            right = idx+arr[idx]
            if right < n and right not in visited:
                queue.append(right)
                visited.add(right)

        return False
