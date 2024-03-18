"""
日期: 2023-11-16
题目: 组合
链接: https://leetcode-cn.com/problems/combinations/
"""

from typing import *
from collections import *
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        cur = []
        def dfs(start: int):
            cur.append(start)
            if len(cur) == k:

                ans.append(cur[:])
            else:
                for i in range(start + 1, n + 2 - (k - len(cur))):
                    dfs(i)
            cur.pop()
        for i in range(1, n + 2 - k):
            dfs(i)
        return ans
    
"""
--TESTCASE BEGIN--
TestCase 0: 4,2
TestCase 1: 1,1
--TESTCASE END--
""" 

print(Solution().combine(4,2))