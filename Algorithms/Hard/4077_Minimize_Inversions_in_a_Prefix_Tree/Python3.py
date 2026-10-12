from math import inf
from bisect import bisect_left

class Solution:
    def minInversions(self, words: list[str], target: list[int]) -> int:
        n = len(words)
        pos = [0] * n
        for p, idx in enumerate(target):
            pos[idx] = p

        trie, mark = [{}], [-1]
        for i, w in enumerate(words):
            u = 0
            for c in w:
                if c not in trie[u]:
                    trie[u][c] = len(trie)
                    trie.append({})
                    mark.append(-1)
                
                u = trie[u][c]
            
            mark[u] = i

        def cross(A: list[int], B: list[int]) -> int:
            count, j = 0, 0
            for x in A:
                while j < len(B) and B[j] < x:
                    j += 1
                
                count += j
            
            return count

        def dfs(u: int) -> tuple[list[int], int]:
            total, lists = 0, []
            for v in trie[u].values():
                L, inv = dfs(v)
                total += inv
                lists.append(L)

            c = len(lists)
            if c >= 2:
                cost = [[0] * c for _ in range(c)]
                for a in range(c):
                    for b in range(a + 1, c):
                        x = cross(lists[a], lists[b])
                        cost[a][b] = x
                        cost[b][a] = len(lists[a]) * len(lists[b]) - x

                full, add = 1 << c, []
                for j in range(c):
                    arr = [0] * full
                    for mask in range(1, full):
                        low = mask & -mask
                        arr[mask] = arr[mask ^ low] + cost[low.bit_length() - 1][j]
                    
                    add.append(arr)

                dp = [inf] * full
                dp[0] = 0
                for mask in range(full):
                    if dp[mask] == inf:
                        continue
                    
                    for j in range(c):
                        bit = 1 << j
                        if not mask & bit:
                            nd = dp[mask] + add[j][mask]
                            if nd < dp[mask | bit]:
                                dp[mask | bit] = nd
                
                total += dp[full - 1]

            merged = []
            for L in lists:
                merged += L
            
            merged.sort()
            if mark[u] >= 0:
                total += bisect_left(merged, pos[mark[u]])
                merged.append(pos[mark[u]])
                merged.sort()

            return merged, total

        return dfs(0)[1]
