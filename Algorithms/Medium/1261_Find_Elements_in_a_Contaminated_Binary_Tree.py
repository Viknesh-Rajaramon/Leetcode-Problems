from imports import *

class FindElements:
    def __init__(self, root: Optional[TreeNode]):
        def recoverTree(root: Optional[TreeNode], x: int) -> None:
            if not root:
                return
            
            self.binary_tree.add(x)
            root.left = recoverTree(root.left, 2*x+1)
            root.right = recoverTree(root.right, 2*x+2)
        
        self.binary_tree = set()
        recoverTree(root, 0)

    def find(self, target: int) -> bool:
        return target in self.binary_tree


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
