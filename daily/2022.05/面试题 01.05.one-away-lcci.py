"""
日期: 2022-05-13
题目: 一次编辑
链接: https://leetcode-cn.com/problems/one-away-lcci/
"""

from typing import *
from collections import *

class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        m, n = len(first), len(second)
        if abs(m - n) > 2:
            return False
        if first == second:
            return True
        
        if m == n:
            count = 0
            for i in range(m):
                if first[i] != second[i]:
                    count += 1
                    if count > 1:
                        return False
            return True
        
        if m != n:
            if m < n:
                first, second = second, first
                m, n = n, m
            i = 0

            if second == "":
                return True

            for i in range(m):
                if first[i] != second[i]:
                    break
            
            for j in range(i + 1, m):
                if first[j] != second[j - 1]:
                    return False
            return True


                
        
        