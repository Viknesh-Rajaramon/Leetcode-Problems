from imports import *

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings = sorted(meetings, key = lambda x: x[0])
        
        unused_rooms, used_rooms = list(range(n)), []
        heapify(unused_rooms)

        counts = [0] * n
        for start, end in meetings:
            while used_rooms and used_rooms[0][0] <= start:
                _, room = heappop(used_rooms)
                heappush(unused_rooms, room)
            
            time = end
            if unused_rooms:
                room = heappop(unused_rooms)
            else:
                prev_end, room = heappop(used_rooms)
                time += prev_end - start
            
            counts[room] += 1
            heappush(used_rooms, (time, room))
        
        return max(range(n), key = lambda x: (counts[x], -x))
