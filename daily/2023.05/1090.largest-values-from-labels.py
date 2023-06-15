"""
日期: 2023-05-23
题目: 受标签影响的最大值
链接: https://leetcode-cn.com/problems/largest-values-from-labels/
"""

from typing import *
from collections import *
class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int: