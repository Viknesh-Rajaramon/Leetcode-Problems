from imports import *

class Solution:
    def getAllElements(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> List[int]:
        def dfs(node: Optional[TreeNode], bst: List[int]) -> None:
            if not node:
                return
            
            dfs(node.left, bst)
            bst.append(node.val)
            dfs(node.right, bst)
        
        list1, list2 = [], []
        dfs(root1, list1)
        dfs(root2, list2)
        
        result, i, j = [], 0, 0
        while i < len(list1) and j < len(list2):
            if list1[i] <= list2[j]:
                result.append(list1[i])
                i += 1
            else:
                result.append(list2[j])
                j += 1
            
        while i < len(list1):
            result.append(list1[i])
            i += 1
        
        while j < len(list2):
            result.append(list2[j])
            j += 1

        return result
