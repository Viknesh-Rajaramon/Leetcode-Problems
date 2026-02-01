from typing import List
from collections import deque

class RideSharingSystem:

    def __init__(self):
        self.rider = deque()
        self.driver = deque()
        self.track = set()

    def addRider(self, riderId: int) -> None:
        self.rider.append(riderId)
        self.track.add(riderId)

    def addDriver(self, driverId: int) -> None:
        self.driver.append(driverId)

    def matchDriverWithRider(self) -> List[int]:
        if not self.driver:
            return [-1, -1]

        while self.rider:
            rider_id = self.rider.popleft()
            if rider_id in self.track:
                self.track.remove(rider_id)
                return [self.driver.popleft(), rider_id]
        
        return [-1, -1]

    def cancelRider(self, riderId: int) -> None:
        if riderId in self.track:
            self.track.remove(riderId)


# Your RideSharingSystem object will be instantiated and called as such:
# obj = RideSharingSystem()
# obj.addRider(riderId)
# obj.addDriver(driverId)
# param_3 = obj.matchDriverWithRider()
# obj.cancelRider(riderId)
