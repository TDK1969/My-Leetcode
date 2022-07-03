"""
日期: 2022-06-27
题目: 最长特殊序列 II
链接: https://leetcode-cn.com/problems/longest-uncommon-subsequence-ii/
"""

from typing import *
from collections import *
class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def check(long: str, short: str) -> bool:
            j = 0
            for j in len(long):
                if long[j] == short[i]:
                    i += 1
                    if i == len(short):
                        return True
                j += 1
            
            return False
        
        strs.sort(reverse=True)
        n = len(strs)
        

            
            
