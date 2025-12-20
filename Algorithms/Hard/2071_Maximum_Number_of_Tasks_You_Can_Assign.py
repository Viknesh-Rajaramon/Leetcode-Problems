from typing import List
from sortedcontainers import SortedList

class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        n, m = len(tasks), len(workers)
        tasks.sort()
        workers.sort()

        def check(mid: int) -> bool:
            p = pills
            workers_sorted = SortedList(workers[m - mid : ])
            for i in range(mid - 1, -1, -1):
                if workers_sorted[i] >= tasks[i]:
                    workers_sorted.pop()
                else:
                    if p == 0:
                        return False
                    
                    rep = workers_sorted.bisect_left(tasks[i] - strength)
                    if rep == len(workers_sorted):
                        return False
                    
                    p -= 1
                    workers_sorted.pop(rep)
            
            return True

        result = 0
        low, high = 1, min(n, m)
        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                result = mid
                low = mid + 1
            else:
                high = mid - 1
        
        return result
