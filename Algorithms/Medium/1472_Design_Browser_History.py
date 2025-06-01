class DLLNode:
    def __init__(self, url="", prev=None, next=None):
        self.url = url
        self.prev = prev
        self.next = next

class BrowserHistory:

    def __init__(self, homepage: str):
        self.ptr = DLLNode(homepage)

    def visit(self, url: str) -> None:
        node = DLLNode(url)
        self.ptr.next = node
        node.prev = self.ptr
        self.ptr = self.ptr.next

    def back(self, steps: int) -> str:
        while self.ptr.prev and steps > 0:
            self.ptr = self.ptr.prev
            steps -= 1

        return self.ptr.url

    def forward(self, steps: int) -> str:
        while self.ptr.next and steps > 0:
            self.ptr = self.ptr.next
            steps -= 1

        return self.ptr.url

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
