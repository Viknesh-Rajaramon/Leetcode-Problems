from imports import *

class Router:

    def __init__(self, memoryLimit: int):
        self.s = set()
        self.queue = deque()
        self.destination_timestamp_map = defaultdict(SortedList)
        self.memory_limit = memoryLimit

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        if (source, destination, timestamp) in self.s:
            return False
        
        if len(self.queue) == self.memory_limit:
            oldest_packet = self.queue.popleft()
            self.destination_timestamp_map[oldest_packet[1]].remove(oldest_packet[2])
            self.s.remove(oldest_packet)
        
        self.queue.append((source, destination, timestamp))
        self.destination_timestamp_map[destination].add(timestamp)
        self.s.add((source, destination, timestamp))
        return True

    def forwardPacket(self) -> List[int]:
        if len(self.queue) == 0:
            return []

        source, destination, timestamp = self.queue.popleft()
        self.destination_timestamp_map[destination].remove(timestamp)
        self.s.remove((source, destination, timestamp))
        return [source, destination, timestamp]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        timestamps = self.destination_timestamp_map[destination]
        left = timestamps.bisect_left(startTime)
        right = timestamps.bisect_right(endTime)
        return right - left

# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)
