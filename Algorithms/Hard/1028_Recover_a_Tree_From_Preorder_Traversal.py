from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        depth = 0
        i = 0
        stack = []

        while i < len(traversal):
            if traversal[i] == "-":
                depth += 1
                i += 1
            else:
                j = i
                while j < len(traversal):
                    if traversal[j] == "-":
                        break
                    
                    j += 1
                
                num = int(traversal[i : j])
                node = TreeNode(num)

                if len(stack) > depth:
                    stack = stack[: depth]
                
                if stack and not stack[-1].left:
                    stack[-1].left = node
                elif stack:
                    stack[-1].right = node
                
                stack.append(node)
                i = j
                depth = 0
        
        return stack[0]
