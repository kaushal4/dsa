class TaskManager:

    @staticmethod
    def cmp(a, b):
        if a[0] == b[0]:
            return b[1] - a[1]
        return b[0] - a[0]

    def __init__(self, tasks: List[List[int]]):
        self.hash = {}
        self.hp = {}
        self.pq = []
        self.tuple_comp = cmp_to_key(TaskManager.cmp)
        for task in tasks:
            self.hash[task[1]] = task[0]
            self.hp[task[1]] = task[2]
            self.pq.append(self.tuple_comp((task[2], task[1])))
        heapq.heapify(self.pq)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.hash[taskId] = userId
        self.hp[taskId] = priority
        heapq.heappush(self.pq, self.tuple_comp((priority, taskId)))
        

    def edit(self, taskId: int, newPriority: int) -> None:
        self.hp[taskId] = newPriority
        heapq.heappush(self.pq, self.tuple_comp((newPriority, taskId)))
        

    def rmv(self, taskId: int) -> None:
        if taskId in self.hash:
            self.hash.pop(taskId)
        

    def execTop(self) -> int:
        taskId = -1
        userId = -1
        while (taskId not in self.hash) and self.pq:
            (priority, taskId) = heapq.heappop(self.pq).obj
            if priority != self.hp[taskId]:
                taskId = -1

        if taskId in self.hash:
            userId = self.hash[taskId]
            self.rmv(taskId)

        return userId