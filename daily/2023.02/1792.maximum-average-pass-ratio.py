"""
日期: 2023-02-19
题目: 最大平均通过率
链接: https://leetcode-cn.com/problems/maximum-average-pass-ratio/
"""

from typing import *
from collections import *
import heapq
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:  
        h = []
        heapq.heapify(h)

        for pass_stu, total_stu in classes:
            heapq.heappush(h, (pass_stu / total_stu - (pass_stu + 1) / (total_stu + 1), pass_stu, total_stu))
        
        for _ in range(extraStudents):
            heapq.heapreplace(h, (h[0][1] + 1 / h[0][2] + 1 - (h[0][1] + 2 / h[0][2] + 2), h[0][1] + 1, h[0][2] + 1))
        
        s = 0
        for _, a, b in h:
            s += a / b
        
        return s / len(h)
            

test = Solution()
print(test.maxAverageRatio(classes = [[1,2],[3,5],[2,2]], extraStudents = 2))
