from typing import List
import bisect

class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        tasks.sort()
        cnt = 1
        n = len(tasks)
        tasks_count = 0
        rest = sessionTime
        while tasks_count < n:
            index = bisect.bisect_right(tasks, rest)
            if index == 0:
                rest = sessionTime
                cnt += 1
            else:
                rest -= tasks[index - 1]
                tasks.pop(index - 1)
                tasks_count += 1

        return cnt

test = Solution()
print(test.minSessions([1,2,3,4,5],15))