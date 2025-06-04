from imports import *

class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.task_manager = {}
        self.priority_queue = []
        for userId, taskId, priority in tasks:
            self.add(userId, taskId, priority)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.task_manager[taskId] = (userId, priority)
        heappush(self.priority_queue, (-priority, -taskId))

    def edit(self, taskId: int, newPriority: int) -> None:
        userId, _ = self.task_manager[taskId]
        self.add(userId, taskId, newPriority)

    def rmv(self, taskId: int) -> None:
        del self.task_manager[taskId]

    def execTop(self) -> int:
        while self.priority_queue:
            p, t = heappop(self.priority_queue)
            if -t in self.task_manager:
                userId, priority = self.task_manager[-t]
                if priority == -p:
                    self.rmv(-t)
                    return userId

        return -1


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()
