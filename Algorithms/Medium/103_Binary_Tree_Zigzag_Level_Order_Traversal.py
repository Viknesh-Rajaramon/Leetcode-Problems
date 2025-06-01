from imports import *

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        depth_nodes = defaultdict(list)
        
        queue = deque([(root, 0)])
        while queue:
            node, depth = queue.popleft()
            if not node:
                continue

            depth_nodes[depth].append(node.val)

            queue.append((node.left, depth+1))
            queue.append((node.right, depth+1))
        
        return [nodes if depth % 2 == 0 else nodes[::-1] for depth, nodes in depth_nodes.items()]
