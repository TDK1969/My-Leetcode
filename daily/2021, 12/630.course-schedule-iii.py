from typing import List
import heapq
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        n = len(courses)
        validCourses = [courses[i] for i in range(n) if courses[i][0] <= courses[i][1]]
        validCourses.sort(key = (lambda x:[x[1], x[0]]))

        attend = []
        Sum = 0
        heapq.heapify(attend)

        for course in validCourses:
            heapq.heappush(attend, -course[0])
            Sum += course[0]
            if sum(attend) > course[1]:
                heapq.heappop(attend)
        return len(attend)



test = Solution()
print(test.scheduleCourse([[5,5],[4,6],[2,6]]))

