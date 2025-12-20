from typing import List
from collections import defaultdict
from math import inf

class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        n = len(nums)
        
        tree = defaultdict(list)
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)

        xor = [0] * n
        parent = [0] * n
        in_time, out_time = [0] * n, [0] * n
        time = 0
        
        stack = [(0, -1, False)]
        while stack:
            node, p, visited = stack.pop()
            if visited:
                xor[node] = nums[node]
                for neighbor in tree[node]:
                    if neighbor != p:
                        xor[node] ^= xor[neighbor]
                
                out_time[node] = time - 1
            else:
                parent[node] = p
                in_time[node] = time
                time += 1
                stack.append((node, p, True))
                for neighbor in reversed(tree[node]):
                    if neighbor != p:
                        stack.append((neighbor, node, False))
        
        result = inf
        for i in range(1, n):
            for j in range(i + 1, n):
                if in_time[i] < in_time[j] <= out_time[i]:
                    x = xor[j]
                    y = xor[i] ^ xor[j]
                elif in_time[j] < in_time[i] <= out_time[j]:
                    x = xor[i]
                    y = xor[i] ^ xor[j]
                else:
                    x = xor[i]
                    y = xor[j]
                
                z = xor[0] ^ x ^ y

                curr_result = max(x, y, z) - min(x, y, z)
                if curr_result < result:
                    result = curr_result
        
        return result
