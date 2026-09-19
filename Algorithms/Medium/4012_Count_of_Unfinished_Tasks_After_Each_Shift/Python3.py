from typing import List
from bisect import bisect_right

class Solution:
    def countTasks(self, tasks: List[int], shifts: List[int]) -> List[int]:
        n = len(tasks)
        for i in range(n-1):
            tasks[i+1] += tasks[i]
        
        result, total, carry = [], tasks[n-1], 0
        for shift in shifts:
            carry += shift
            if carry >= total:
                result.append(0)
                carry = 0
            else:
                result.append(n - bisect_right(tasks, carry))

        return result
