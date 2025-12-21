from collections import defaultdict

class UndergroundSystem:

    def __init__(self):
        self.pending_trips = defaultdict(None)
        self.completed_trips = defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.pending_trips[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.pending_trips[id]
        self.completed_trips[(startStation, stationName)].append(t-startTime)
        self.pending_trips[id] = None

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        trips = self.completed_trips[(startStation, endStation)]
        return sum(trips) / len(trips)


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
