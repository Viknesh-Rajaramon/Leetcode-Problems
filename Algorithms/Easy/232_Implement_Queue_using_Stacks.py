from imports import *

class MyQueue:

    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        stack = []
        while self.queue:
            stack.append(self.queue.pop())
        
        self.queue.append(x)
        while stack:
            self.queue.append(stack.pop())

    def pop(self) -> int:
        return self.queue.pop()

    def peek(self) -> int:
        return self.queue[-1]

    def empty(self) -> bool:
        return False if self.queue else True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
