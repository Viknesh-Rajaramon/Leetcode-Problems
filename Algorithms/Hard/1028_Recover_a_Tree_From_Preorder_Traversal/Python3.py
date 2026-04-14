from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        depth, i, stack = 0, 0, []
        while i < len(traversal):
            if traversal[i] == "-":
                depth += 1
                i += 1
                continue
            
            j = i
            while j < len(traversal):
                if traversal[j] == "-":
                    break
                    
                j += 1
                
            node = TreeNode(int(traversal[i : j]))
            if len(stack) > depth:
                stack = stack[ : depth]
                
            if stack and not stack[-1].left:
                stack[-1].left = node
            elif stack:
                stack[-1].right = node
                
            stack.append(node)
            i, depth = j, 0
        
        return stack[0]
