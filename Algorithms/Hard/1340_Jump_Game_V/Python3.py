from typing import List

class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        result, stack = [1] * n, []

        for i in range(n+1):
            while stack and (i == n or arr[stack[-1]] < arr[i]):
                indices = [stack.pop()]
                while stack and arr[stack[-1]] == arr[indices[0]]:
                    indices.append(stack.pop())
            
                for j in indices:
                    if i < n and i-j <= d:
                        result[i] = max(result[i], result[j]+1)
                    
                    if stack and j-stack[-1] <= d:
                        result[stack[-1]] = max(result[stack[-1]], result[j]+1)
                
            if i < n:
                stack.append(i)

        return max(result)
