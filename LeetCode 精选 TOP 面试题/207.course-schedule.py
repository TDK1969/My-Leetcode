"""
日期: 2022-09-14
题目: 课程表
链接: https://leetcode-cn.com/problems/course-schedule/
"""

from typing import *
from collections import *
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 使用判断是否存在一个合法的拓扑排序判断是否存在一个环
        edges = defaultdict(list)
        in_degree = [0 for _ in range(numCourses)]
        visited = 0

        # 遍历每一条边,记录入度
        for end, start in prerequisites:
            edges[start].append(end)
            in_degree[end] += 1
        
        # 初始化队列为入度为0的节点
        q = deque([i for i in range(numCourses) if in_degree[i] == 0])

        # 访问当前节点,当前节点的入度为0,然后"删除"该节点,即该节点指向的节点入度 - 1,若指向节点入度为0,则入队
        while q:
            t = q.popleft()
            visited += 1
            for nxt in edges[t]:
                in_degree[nxt] -= 1
                
                if in_degree[nxt] == 0:
                    q.append(nxt)
        # 如果存在环,则环中的所有节点都不能入队,因为入度不能降为0
        # 判断能否访问所有节点
        return numCourses == visited


test = Solution()
print(test.canFinish(5, [[1,4],[2,4],[3,1],[3,2]]))
            
