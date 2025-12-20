from typing import List
from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students, sandwiches = deque(students), sandwiches[::-1]
        
        counter = len(students)
        while students and counter > 0:
            if students[0] == sandwiches[-1]:
                sandwiches.pop()
                students.popleft()
                counter = len(students)
            else:
                s = students.popleft()
                students.append(s)
                counter -= 1
        
        return len(students)
