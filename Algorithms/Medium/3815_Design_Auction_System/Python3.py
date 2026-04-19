from collections import defaultdict
from heapq import heappush, heappop

class AuctionSystem:

    def __init__(self):
        self.max_heap = defaultdict(list)
        self.bid_tracker = {}

    def addBid(self, userId: int, itemId: int, bidAmount: int) -> None:
        self.bid_tracker[(userId, itemId)] = bidAmount
        heappush(self.max_heap[itemId], (-bidAmount, -userId))

    def updateBid(self, userId: int, itemId: int, newAmount: int) -> None:
        self.bid_tracker[(userId, itemId)] = newAmount
        heappush(self.max_heap[itemId], (-newAmount, -userId))

    def removeBid(self, userId: int, itemId: int) -> None:
        self.bid_tracker[(userId, itemId)] = 0

    def getHighestBidder(self, itemId: int) -> int:
        while self.max_heap[itemId]:
            bid, user_id = self.max_heap[itemId][0]
            if self.bid_tracker[(-user_id, itemId)] == -bid:
                break
        
            heappop(self.max_heap[itemId])
        
        return -self.max_heap[itemId][0][1] if self.max_heap[itemId] else -1



# Your AuctionSystem object will be instantiated and called as such:
# obj = AuctionSystem()
# obj.addBid(userId,itemId,bidAmount)
# obj.updateBid(userId,itemId,newAmount)
# obj.removeBid(userId,itemId)
# param_4 = obj.getHighestBidder(itemId)
