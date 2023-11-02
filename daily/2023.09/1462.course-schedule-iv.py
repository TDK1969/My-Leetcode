"""
日期: 2023-09-12
题目: 课程表 IV
链接: https://leetcode-cn.com/problems/course-schedule-iv/
"""

from typing import *
from collections import *
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        pre_coureses = [[] for _ in range(numCourses)]
        # b in pre_courses[a] -> a是b的前置课程
        for a, b in prerequisites:
            pre_coureses[a].append(b)
        pre_matrix = [[False for _ in  range(numCourses)] for _ in  range(numCourses)]
        # pre_matrix[x][y] = True -> x是y的前置课程
        is_visited = [False for _ in  range(numCourses)]

        def dfs(start: int):
            if is_visited[start]:
                return
            
            is_visited[start] = True
            for nxt in pre_coureses[start]:
                dfs(nxt)
                pre_matrix[start][nxt] = True
                
                for i in range(numCourses):
                    pre_matrix[start][i] |= pre_matrix[nxt][i]
        
        for i in range(numCourses):
            dfs(i)
        
        ans = []
        for u, v in queries:
            ans.append(pre_matrix[u][v])
        return ans


            
