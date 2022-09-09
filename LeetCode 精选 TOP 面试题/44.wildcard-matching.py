"""
日期: 2022-07-14
题目: 通配符匹配
链接: https://leetcode-cn.com/problems/wildcard-matching/
"""

from typing import *
from collections import *
import functools
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        pp = p[0] if p else ""
        m = len(s)
        
        # 处理连续*的情况
        for i in range(1, len(p)):
            if p[i] == p[i - 1] == "*":
                continue
            pp += p[i]
        p = pp
        n = len(p)
        @functools.lru_cache(None)
        def deal(i: int, j: int) -> bool:
            # 递归函数
            # 处理边界情况

            while i < m and j < n:
                if p[j] == "*":
                    if j == n - 1:
                        return True
                    for k in range(i, m):
                        if s[k] == p[j + 1] or p[j + 1] == "?":
                            if deal(k, j + 1):
                                return True
                    return False
                elif s[i] == p[j] or p[j] == "?":
                    i += 1
                    j += 1
                else:
                    return False
                
            if i == m and j == n:
                return True
            if j == n and i < m:
                return False
            if i == m and j == n - 1 and p[j] == "*":
                return True
            else:
                return False
            
        return deal(0, 0)

test = Solution()
print(test.isMatch("", "**aa*****ba*a*bb**aa*ab****a*aaaaaa***a*aaaa**bbabb*b*b**aaaaaaaaa*a********ba*bbb***a*ba*bb*bb**a*b*bb"))
