from typing import List
from collections import defaultdict, deque

class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        def build_tree(edges: List[List[int]]) -> dict: 
            tree = defaultdict(list)
            for u, v in edges:
                tree[u].append(v)
                tree[v].append(u)
            
            return tree
        
        def bfs(tree: dict):
            queue = deque([(0, True)])
            even_set, odd_set = set([0]), set()

            while queue:
                u, is_even = queue.popleft()

                if is_even:
                    for v in tree[u]:
                        if v in odd_set:
                            continue
                        
                        queue.append((v, False))
                        odd_set.add(v)
                else:
                    for v in tree[u]:
                        if v in even_set:
                            continue
                        
                        queue.append((v, True))
                        even_set.add(v)
            
            return even_set, odd_set

        tree2 = build_tree(edges2)
        even_set_tree2, odd_set_tree2 = bfs(tree2)
        max_node = max(len(even_set_tree2), len(odd_set_tree2))
        
        tree1 = build_tree(edges1)
        even_set_tree1, odd_set_tree1 = bfs(tree1)

        n = len(edges1)+1
        even_length = len(even_set_tree1)
        result = [n - even_length + max_node] * n

        for i in even_set_tree1:
            result[i] = even_length + max_node
        
        return result
