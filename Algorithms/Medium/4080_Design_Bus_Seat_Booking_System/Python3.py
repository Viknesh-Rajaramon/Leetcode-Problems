class BusBooking:

    def __init__(self, n: int):
        self.cost = {}
        self.total_time = 0
        self.min_time = 0
        
    def toggle(self, seat: str) -> None:
        if seat in self.cost:
            self.total_time -= self.cost[seat]
            del self.cost[seat]
            self.min_time -= 1
            return

        c = 1
        if seat[0] == 'A' or seat[0] == 'D':
            middle = 'B' if seat[0] == 'A' else 'C' 
            if middle + seat[1 : ] in self.cost:
                c = 3
        
        self.cost[seat] = c
        self.total_time += c
        self.min_time += 1

    def getTotalTime(self) -> int:
        return self.total_time

    def getMinTime(self) -> int:
        return self.min_time


# Your BusBooking object will be instantiated and called as such:
# obj = BusBooking(n)
# obj.toggle(seat)
# param_2 = obj.getTotalTime()
# param_3 = obj.getMinTime()
