from imports import *

class Node:
    def __init__(self, name="", alive=True):
        self.name = name
        self.alive=True
        self.children = []

class ThroneInheritance:

    def __init__(self, kingName: str):
        self.root = Node(name = kingName)
        self.hash_map = {kingName: self.root}

    def birth(self, parentName: str, childName: str) -> None:
        child = Node(childName)
        self.hash_map[childName] = child
        parent = self.hash_map[parentName]
        parent.children.append(child)

    def death(self, name: str) -> None:
        self.hash_map[name].alive = False

    def getInheritanceOrder(self) -> List[str]:
        result = []

        def dfs(parent: Node):
            if not parent:
                return
            
            if parent.alive:
                result.append(parent.name)
            
            for child in parent.children:
                dfs(child)

        dfs(self.root)
        return result


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()
