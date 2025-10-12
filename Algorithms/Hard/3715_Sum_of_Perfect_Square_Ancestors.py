from imports import *

class Solution:
    def sumOfAncestors(self, n: int, edges: List[List[int]], nums: List[int]) -> int:
        tree = defaultdict(list)
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)
        
        def get_parity_sum(num: int) -> str:
            parity = []
            for i in range(2, int(sqrt(num)) + 2):
                count = 0
                while num % i == 0:
                    num //= i
                    count += 1
                
                if count & 1:
                    parity.append(i)
            
            if num > 1:
                parity.append(num)
            
            return "#".join(list(map(str, parity)))
        
        result = 0
        def dfs(x: int, parity: int, curr_fre: defaultdict) -> None:
            nonlocal result

            curr_str = get_parity_sum(nums[x])
            if curr_str in curr_fre:
                result += curr_fre[curr_str]
            
            curr_fre[curr_str] += 1
            for neighbor in tree[x]:
                if neighbor != parity:
                    dfs(neighbor, x, curr_fre)
            
            curr_fre[curr_str] -= 1
        
        dfs(0, -1, defaultdict(int))
        return result
