from typing import List
from collections import defaultdict, Counter

class Solution:
    def interactionCosts(self, n: int, edges: List[List[int]], group: List[int]) -> int:
        tree, group_count = defaultdict(list), Counter(group)
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)

        result = 0
        def dfs(u: int, parent: int) -> defaultdict:
            nonlocal result
            count = defaultdict(int)
            count[group[u]] += 1

            for v in tree[u]:
                if v == parent:
                    continue

                child = dfs(v, u)
                for g, val in child.items():
                    if g == 0:
                        continue
                    
                    result += val * (group_count[g] - val)
                    count[g] += val

            return count

        dfs(0, -1)
        return result
