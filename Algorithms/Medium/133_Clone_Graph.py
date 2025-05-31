from imports import *

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        deep_copy = {}

        def dfs(node: Optional['Node']) -> Optional['Node']:
            deep_copy[node] = Node(node.val)
            for neighbor in node.neighbors:
                if neighbor in deep_copy:
                    deep_copy[node].neighbors.append(deep_copy[neighbor])
                else:
                    deep_copy[node].neighbors.append(dfs(neighbor))
            
            return deep_copy[node]

        return dfs(node) if node else None
