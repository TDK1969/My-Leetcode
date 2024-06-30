"""
日期: 2024-03-26
题目: 设计可以求最短路径的图类
链接: https://leetcode.cn/problems/design-graph-with-shortest-path-calculator/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Graph:

    def __init__(self, n: int, edges: List[List[int]]):


    def addEdge(self, edge: List[int]) -> None:


    def shortestPath(self, node1: int, node2: int) -> int:



# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)

"""
--TESTCASE BEGIN--
TestCase 0: ["Graph","shortestPath","shortestPath","addEdge","shortestPath"],[[4,[[0,2,5],[0,1,2],[1,2,1],[3,0,3]]],[3,2],[0,3],[[1,3,4]],[0,3]]
--TESTCASE END--
""" 
