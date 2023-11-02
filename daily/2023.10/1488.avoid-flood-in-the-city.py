"""
日期: 2023-10-13
题目: 避免洪水泛滥
链接: https://leetcode-cn.com/problems/avoid-flood-in-the-city/
"""

from typing import *
from collections import *
from sortedcontainers import SortedList
class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        ans = [1 for _ in range(n)]
        lakes = dict()
        capable_days = SortedList()
        
        for i, v in enumerate(rains):
            if v > 0:
                ans[i] = -1
                if v in lakes:
                    index = capable_days.bisect(lakes[v])
                    if index == len(capable_days):
                        return []
                    ans[capable_days[index]] = v
                    capable_days.discard(capable_days[index])    
                lakes[v] = i
            else:
                capable_days.add(i)
        return ans


