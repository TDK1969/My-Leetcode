"""
题目: 判断两个事件是否存在冲突
链接: https://leetcode-cn.com/problems/determine-if-two-events-have-conflict/
"""

from typing import *
from collections import *
class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        event1_start = int(event1[0][:2]) * 60 + int(event1[0][3:])
        event1_end = int(event1[1][:2]) * 60 + int(event1[1][3:])

        event2_start = int(event2[0][:2]) * 60 + int(event2[0][3:])
        event2_end = int(event2[1][:2]) * 60 + int(event2[1][3:])

        return not (event1_start < event1_end < event2_start < event2_end or event2_start < event2_end < event1_start < event1_end)
        