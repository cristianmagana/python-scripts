import heapq
from dataclasses import dataclass, field
from typing import Any

@dataclass(order=True)
class Task:
    priority: int  # Lower number = higher priority
    task_id: str = field(compare=False)
    data: Any = field(compare=False)

class JobScheduler:
    def __init__(self):
        self.queue = []  # Min heap
    
    def add_task(self, task_id: str, priority: int, data: Any):
        """Add a task to the queue"""
        task = Task(priority, task_id, data)
        heapq.heappush(self.queue, task)
    
    def get_next_task(self):
        """Get highest priority task"""
        if not self.queue:
            return None
        return heapq.heappop(self.queue)
    
    def size(self):
        return len(self.queue)

# Usage
scheduler = JobScheduler()
scheduler.add_task("backup", priority=2, data={"type": "backup"})
scheduler.add_task("critical", priority=1, data={"type": "alert"})
scheduler.add_task("cleanup", priority=3, data={"type": "cleanup"})

task = scheduler.get_next_task()
print(f"Processing: {task.task_id} with priority {task.priority}")
# Output: Processing: critical with priority 1