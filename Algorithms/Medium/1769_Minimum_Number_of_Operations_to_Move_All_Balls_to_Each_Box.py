from imports import *

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)

        left = [0] * n
        right = [0] * n
        
        count = 0
        for i in range(1, n):
            if boxes[i-1] == "1":
                count += 1
            
            left[i] = left[i-1] + count
        
        count = 0
        for i in range(n-2, -1, -1):
            if boxes[i+1] == "1":
                count += 1
            
            right[i] = right[i+1] + count
        
        ans = [0] * n
        for i in range(n):
            ans[i] = left[i] + right[i]
        
        return ans
