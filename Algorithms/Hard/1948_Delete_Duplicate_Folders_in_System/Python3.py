from typing import List
from collections import defaultdict

class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        tree = {}
        for path in paths:
            curr = tree
            for name in path:
                curr = curr.setdefault(name, {})

        store = defaultdict(list)
        def encode(node: dict) -> str:
            if not node:
                return "()"
            
            parts = [key + encode(sub) for key, sub in node.items()]
            sign = "".join(sorted(parts))
            store[sign].append(node)
            return "(" + sign + ")"
        
        def remove(nodes: List[dict]) -> None:
            for item in nodes:
                item.clear()
                item["#"] = True

        def collect(node: str, path: List[str]) -> None:
            for key, sub in list(node.items()):
                if "#" in sub:
                    continue
                
                new = path + [key]
                result.append(new)
                collect(sub, new)
        
        encode(tree)
        for group in store.values():
            if len(group) > 1:
                remove(group)
        
        result = []
        collect(tree, [])
        return result
