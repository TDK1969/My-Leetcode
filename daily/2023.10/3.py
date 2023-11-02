from typing import List
import heapq

class Task:
    def __init__(self, id: int, r: int, p: int ) -> None:
        self.id = id
        self.r = r
        self.p = p


def processTasks(tasks: List[Task]) -> List[List[int]]:
    release_tasks_list = sorted(tasks, key=lambda task:task.r)
    n = len(release_tasks_list)
    p = 0
    h = []
    ans = []
    heapq.heapify(h)

    cur_time = 0
    
    while h or p < n:
        # 发布任务
        while p < n and cur_time == release_tasks_list[p].r:
            heapq.heappush(h, [release_tasks_list[p].p, release_tasks_list[p].id])
            p += 1
        
        # 如有,执行任务
        task_finish_time = float("inf")
        has_task = False
        if len(h) != 0:
            has_task = True
            cur_task = heapq.heappop(h)
            task_finish_time = cur_time + cur_task[0]

        nxt_task_release_time = float("inf")
        if p < n:
            nxt_task_release_time = release_tasks_list[p].r
        
        nxt_key_time = min(nxt_task_release_time, task_finish_time)
        if has_task:
            if nxt_key_time - cur_time < cur_task[0]:
                cur_task[0] -= nxt_key_time - cur_time
                heapq.heappush(h, cur_task)
            else:
                ans.append([cur_task[1], nxt_key_time])
        cur_time = nxt_key_time
    
    return ans


input_str = input()
input_list = list(map(int, input_str.split()))[1:]
task_list = []
for i in range(0, len(input_list), 2):
    task_list.append(Task((i >> 1) + 1, input_list[i], input_list[i + 1]))
print(processTasks(task_list))
        

        







        
    