from imports import *

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        queue = deque()
        k = 0

        for i in range(len(nums)):
            if nums[i] == val:
                queue.append(i)
            else:
                k += 1
                if len(queue) > 0:
                    index = queue.popleft()
                    nums[index] = nums[i]
                    queue.append(i)
        
        return k
