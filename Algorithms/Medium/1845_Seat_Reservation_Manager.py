from imports import *

class SeatManager:

    def __init__(self, n: int):
        self.unreserved_seats = list(range(n))

    def reserve(self) -> int:
        return heappop(self.unreserved_seats)+1

    def unreserve(self, seatNumber: int) -> None:
        heappush(self.unreserved_seats, seatNumber-1)



# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)
