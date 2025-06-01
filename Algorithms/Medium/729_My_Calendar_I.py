from imports import *

class MyCalendar:

    def __init__(self):
        self.calendar = []

    def book(self, startTime: int, endTime: int) -> bool:
        index = bisect_left(self.calendar, (startTime, endTime))
        
        if index > 0 and self.calendar[index-1][1] > startTime:
            return False
        
        if index < len(self.calendar) and self.calendar[index][0] < endTime:
            return False
        
        self.calendar.insert(index, (startTime, endTime))        
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)
