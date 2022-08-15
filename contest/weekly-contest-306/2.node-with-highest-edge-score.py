"""
题目: 边积分最高的节点
链接: https://leetcode-cn.com/problems/node-with-highest-edge-score/
"""

from typing import *
from collections import *
class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        score = dict()
        for i, v in enumerate(edges):
            if v not in score:
                score[v] = 0
            score[v] += i
        score = [[i, score[i]] for i in score.keys()]
        score.sort(key=lambda x:[-x[1], x[0]])
        return score[0][0]

test = Solution()
print(test.edgeScore(edges = [1,0,0,0,0,7,7,5]))

            