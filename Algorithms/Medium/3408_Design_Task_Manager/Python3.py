from typing import List
from heapq import heapify, heappop, heappush

class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.manager = {}
        self.tasks = []

        for user, task, priority in tasks:
            t = (-priority, -task, user)
            self.manager[-task] = t
            self.tasks.append(t)
        
        heapify(self.tasks)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        t = (-priority, -taskId, userId)
        self.manager[-taskId] = t
        heappush(self.tasks, t)

    def edit(self, taskId: int, newPriority: int) -> None:
        _, old_task, old_user = self.manager[-taskId]
        t = (-newPriority, old_task, old_user)
        self.manager[old_task] = t
        heappush(self.tasks, t)

    def rmv(self, taskId: int) -> None:
        del self.manager[-taskId]

    def execTop(self) -> int:
        while self.tasks:
            p, t, u = heappop(self.tasks)
            if t not in self.manager:
                continue
            
            if self.manager[t][0] != p or self.manager[t][2] != u:
                continue
                
            del self.manager[t]
            return u

        return -1


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()
