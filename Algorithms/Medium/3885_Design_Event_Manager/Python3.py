from heapq import heappush, heappop, heapify

class EventManager:

    def __init__(self, events: list[list[int]]):
        self.hash_map = {}
        self.max_heap = []
        for event_id, priority in events:
            self.hash_map[event_id] = priority
            self.max_heap.append((-priority, event_id))
        
        heapify(self.max_heap)

    def updatePriority(self, eventId: int, newPriority: int) -> None:
        self.hash_map[eventId] = newPriority
        heappush(self.max_heap, (-newPriority, eventId))

    def pollHighest(self) -> int:
        while self.max_heap:
            priority, event_id = heappop(self.max_heap)
            if self.hash_map[event_id] == -priority:
                self.hash_map[event_id] = -1
                return event_id

        return -1


# Your EventManager object will be instantiated and called as such:
# obj = EventManager(events)
# obj.updatePriority(eventId,newPriority)
# param_2 = obj.pollHighest()
