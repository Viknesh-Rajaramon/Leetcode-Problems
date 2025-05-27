from imports import *

class Solution:
    def __init__(self, head: Optional[ListNode]):
        self.head = head
        self.n = 0
        ptr = head
        while ptr:
            self.n += 1
            ptr = ptr.next

    def getRandom(self) -> int:
        index = randint(0, self.n-1)
        ptr = self.head
        while index:
            ptr = ptr.next
            index -= 1
        
        return ptr.val


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
