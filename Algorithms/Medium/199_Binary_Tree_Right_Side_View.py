from imports import *

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        level_nodes = defaultdict(list)

        queue = deque([(root, 0)])
        while queue:
            node, depth = queue.popleft()
            if not node:
                continue
            
            level_nodes[depth].append(node.val)
            
            if node.left:
                queue.append((node.left, depth+1))
            
            if node.right:
                queue.append((node.right, depth+1))
        
        result = []
        for depth, nodes in level_nodes.items():
            result.append(nodes[-1])
        
        return result
