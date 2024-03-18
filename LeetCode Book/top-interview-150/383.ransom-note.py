"""
日期: 2023-11-01
题目: 赎金信
链接: https://leetcode-cn.com/problems/ransom-note/
"""

from typing import *
from collections import *
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rc = Counter(ransomNote)
        mc = Counter(magazine)

        for alpha in rc.keys():
            if rc[alpha] > mc[alpha]:
                return False
        return True