"""
日期: 2023-09-11
题目: 课程表 III
链接: https://leetcode-cn.com/problems/course-schedule-iii/
"""

from typing import *
from collections import *
import heapq

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x:(x[1], x[0]))
        h = []
        heapq.heapify(h)
        time_sum = 0
        for duration, ddl in courses:
            if time_sum + duration <= ddl:
                time_sum += duration
                heapq.heappush(h, -duration)
            else:
                if len(h) > 0 and duration < -heapq.nsmallest(1, h)[0]:
                    t = -heapq.heappop(h)
                    time_sum  = time_sum - t + duration
                    heapq.heappush(h, -duration)

        return len(h)

test = Solution()
print(test.scheduleCourse([[5,5],[4,6],[2,6]]))
        