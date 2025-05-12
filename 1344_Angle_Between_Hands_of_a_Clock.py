class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        minutes_angle = minutes*6
        hours_angle = (hour*30) + (minutes/2)
        
        return min(abs(hours_angle-minutes_angle), 360-abs(hours_angle-minutes_angle))
