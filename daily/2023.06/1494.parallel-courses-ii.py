"""
日期: 2023-06-16
题目: 并行课程 II
链接: https://leetcode-cn.com/problems/parallel-courses-ii/
"""

from typing import *
from collections import *
class Solution:
    def minNumberOfSemesters(self, n: int, relations: List[List[int]], k: int) -> int:
        pre_lesson = [0] * (n + 1)
        nxt_lesson = [[] for _ in range(n + 1)]

        for i, j in relations:
            pre_lesson[j] |= 1 << i
            nxt_lesson[i].append(j)
        
        t = [0] * (n + 1)

        this_term_quere = deque()
        for i in range(1, n + 1):
            if pre_lesson[i] == 0:
                this_term_quere.append(i)
        next_term_queue = this_term_quere.copy()
        
        cnt = 0
        ans = 0

        while cnt < n:
            for _ in range(k):
                if len(this_term_quere) == 0:
                    break
                lesson = this_term_quere.popleft()
                next_term_queue.popleft()
                cnt += 1
                for nxt in nxt_lesson[lesson]:
                    t[nxt] |= 1 << lesson
                    if t[nxt] == pre_lesson[nxt]:
                        next_term_queue.append(nxt)
            ans += 1
            this_term_quere = next_term_queue.copy()
        
        return ans

test = Solution()
print(test.minNumberOfSemesters(n = 4, relations = [[2,1],[3,1],[1,4]], k = 2))
                    

        
    