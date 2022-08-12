"""
日期: 2022-08-12
题目: 用户分组
链接: https://leetcode-cn.com/problems/group-the-people-given-the-group-size-they-belong-to/
"""

from typing import *
from collections import *
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        ans = []
        group = defaultdict(list)
        for i, group_size in enumerate(groupSizes):
            group[group_size].append(i)
            if len(group[group_size]) == group_size:
                ans.append(group[group_size])
                group[group_size] = []
        return ans