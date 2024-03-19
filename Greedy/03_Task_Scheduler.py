# https://leetcode.com/problems/task-scheduler/
# 621. Task Scheduler

"BEATS 98.99%"
from typing import List
from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counts = list(Counter(tasks).values())
        max_task = max(task_counts)
        max_count = task_counts.count(max_task)
        return max(len(tasks), (max_task - 1) * (n + 1) + max_count)
# MAX OF
    # no of slots * (length of slots+1(for the beginning of the task)) + no of tasks with max count
    # len(tasks) -- if all tasks dont accomodate inside the slot as seen below
if __name__=="__main__":
    s=Solution()
    tasks=["A","A","B","C","E"]
    n=2
    print(s.leastInterval(tasks,n))

