from imports import *

class Router:

    def __init__(self, memoryLimit: int):
        self.packets = set()
        self.queue = deque()
        self.destination_timestamp_map = defaultdict(list)
        self.memory_limit = memoryLimit

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        packet = (source, destination, timestamp)
        if packet in self.packets:
            return False
        
        if len(self.queue) == self.memory_limit:
            oldest_packet = self.queue.popleft()
            self.packets.remove(oldest_packet)
            old_src, old_dst, old_time = oldest_packet
            idx = bisect_left(self.destination_timestamp_map[old_dst], old_time)
            del self.destination_timestamp_map[old_dst][idx]
        
        self.queue.append(packet)
        self.packets.add(packet)
        insort(self.destination_timestamp_map[destination], timestamp)
        return True

    def forwardPacket(self) -> List[int]:
        if len(self.queue) == 0:
            return []

        packet = self.queue.popleft()
        self.packets.remove(packet)
        source, destination, timestamp = packet
        idx = bisect_left(self.destination_timestamp_map[destination], timestamp)
        del self.destination_timestamp_map[destination][idx]
        return [source, destination, timestamp]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        if destination not in self.destination_timestamp_map:
            return 0
        
        timestamps = self.destination_timestamp_map[destination]
        left = bisect_left(timestamps, startTime)
        right = bisect_right(timestamps, endTime)
        return right - left

# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)
