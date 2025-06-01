class DLLNode:
    def __init__(self, key = 0, val = 0, prev = None, next = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.curr_capacity = 0
        self.cache = {}
        self.head = DLLNode()
        self.tail = DLLNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: DLLNode) -> None:
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        self.cache[node.key] = None
        self.curr_capacity -= 1

    def _add(self, node: DLLNode) -> None:
        self.cache[node.key] = node
        prev_node = self.tail.prev
        self.tail.prev = node
        node.next = self.tail
        node.prev = prev_node
        prev_node.next = node
        self.curr_capacity += 1

    def get(self, key: int) -> int:
        if key not in self.cache or not self.cache[key]:
            return -1
        
        node = self.cache[key]
        self._remove(node)
        self._add(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache and self.cache[key]:
            self.cache[key].val = value
            node = self.cache[key]
            self._remove(node)
            self._add(node)
            return

        if self.curr_capacity >= self.capacity:
            self._remove(self.head.next)
        
        node = DLLNode(key, value)
        self._add(node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
