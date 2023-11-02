"""
日期: 2023-10-23
题目: 老人的数目
链接: https://leetcode-cn.com/problems/number-of-senior-citizens/
"""

from typing import *
from collections import *
class Solution:
    def countSeniors(self, details: List[str]) -> int:
        return len([i for i in details if int(i[11:13]) > 60])