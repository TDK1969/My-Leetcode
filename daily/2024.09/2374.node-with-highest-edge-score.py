"""
日期: 2024-09-21
题目: 边积分最高的节点
链接: https://leetcode.cn/problems/node-with-highest-edge-score/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        max_score = -1
        n = len(edges)
        scores = [0 for _ in range(n)]
        ans = -1
        for i in range(n):
            scores[edges[i]] += i
            if scores[edges[i]] > max_score:
                ans = edges[i]
                max_score = scores[edges[i]]
            elif scores[edges[i]] == max_score and edges[i] < ans:
                ans = edges[i]

        return ans

"""
--TESTCASE BEGIN--
TestCase 0: [1,0,0,0,0,7,7,5]
TestCase 1: [2,0,0,2]
--TESTCASE END--
""" 
