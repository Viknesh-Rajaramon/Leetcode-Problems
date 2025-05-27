from imports import *

class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def constructTree(index: List[int], low: int, high: int) -> Optional[TreeNode]:
            if index[0] >= len(preorder) or low > high:
                return None
            
            root = TreeNode(preorder[index[0]])
            index[0] += 1

            if low == high:
                return root
            
            i = low
            while i <= high:
                if preorder[index[0]] == postorder[i]:
                    break
                
                i += 1
            
            if i <= high:
                root.left = constructTree(index, low, i)
                root.right = constructTree(index, i+1, high-1)

            return root
        
        return constructTree([0], 0, len(preorder)-1)
