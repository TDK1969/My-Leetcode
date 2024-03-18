"""
日期: 2023-12-25
题目: 课程表 II
链接: https://leetcode-cn.com/problems/course-schedule-ii/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        edges = defaultdict(list)
        in_degree = [0 for _ in range(numCourses)]
        ans = []

        # 遍历每一条边,记录入度
        for end, start in prerequisites:
            edges[start].append(end)
            in_degree[end] += 1
        
        # 初始化队列为入度为0的节点
        q = deque([i for i in range(numCourses) if in_degree[i] == 0])

        # 访问当前节点,当前节点的入度为0,然后"删除"该节点,即该节点指向的节点入度 - 1,若指向节点入度为0,则入队
        while q:
            t = q.popleft()
            ans.append(t)
            for nxt in edges[t]:
                in_degree[nxt] -= 1
                
                if in_degree[nxt] == 0:
                    q.append(nxt)
        
        if len(ans) != numCourses:
            return []  
        return ans
"""
--TESTCASE BEGIN--
TestCase 0: 2,[[1,0]]
TestCase 1: 4,[[1,0],[2,0],[3,1],[3,2]]
TestCase 2: 1,[]
--TESTCASE END--
""" 

print(Solution().findOrder(1,[]))