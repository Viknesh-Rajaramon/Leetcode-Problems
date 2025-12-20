from typing import List

class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()

        result = 0
        for a, b in zip(seats, students):
            result += abs(a-b)
        
        return result
