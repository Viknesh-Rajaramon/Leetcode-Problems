class Solution:
    def weightedSum(self, parent: list[int], nums: list[int]) -> int:
        n = len(parent)
        tree, depth = [[] for _ in range(n)], [-1] * n
        for i in range(1, n):
            tree[parent[i]].append(i)
        
        def dfs(u: int, d: int) -> None:
            depth[u] = d
            for v in tree[u]:
                dfs(v, d+1)
        
        dfs(0, 0)
        
        result, height = 0, max(depth)+1
        for i in range(n):
            result += nums[i] * (height - depth[i])
        
        return result
