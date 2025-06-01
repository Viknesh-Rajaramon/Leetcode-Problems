class DLLNode:
    def __init__(self, value=-1, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

class MyCircularDeque:

    def __init__(self, k: int):
        self.capacity = k
        self.curr_capacity = 0

        self.head = DLLNode()
        self.tail = DLLNode()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _add(self, node: DLLNode, new_node: DLLNode) -> None:
        new_node.prev = node
        new_node.next = node.next
        node.next.prev = new_node
        node.next = new_node
        self.curr_capacity += 1
    
    def _delete(self, node: DLLNode) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev
        self.curr_capacity -= 1

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False

        self._add(self.head, DLLNode(value))
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
            
        self._add(self.tail.prev, DLLNode(value))
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False

        self._delete(self.head.next)
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False

        self._delete(self.tail.prev)
        return True

    def getFront(self) -> int:
        return self.head.next.value

    def getRear(self) -> int:
        return self.tail.prev.value

    def isEmpty(self) -> bool:
        return self.curr_capacity == 0

    def isFull(self) -> bool:
        return self.curr_capacity == self.capacity


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
