"""
日期: 2022-07-14
题目: 字母异位词分组
链接: https://leetcode-cn.com/problems/group-anagrams/
"""

from typing import *
from collections import *
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            d[str(sorted(s))].append(s)
        return list(d.values())