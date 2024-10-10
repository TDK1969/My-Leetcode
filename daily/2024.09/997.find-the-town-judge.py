"""
日期: 2024-09-22
题目: 找到小镇的法官
链接: https://leetcode.cn/problems/find-the-town-judge/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusted_count = [set() for _ in range(n + 1)]
        trust_other_flag = [False for _ in range(n + 1)]

        for a, b in trust:
            trust_other_flag[a] = True
            trusted_count[b].add(a)
        
        ans = []
        for i in range(1, n + 1):
            if not trust_other_flag[i] and len(trusted_count[i]) == n - 1:
                ans.append(i)
        
        if len(ans) == 1:
            return ans[0]
        else:
            return -1



"""
--TESTCASE BEGIN--
TestCase 0: 2,[[1,2]]
TestCase 1: 3,[[1,3],[2,3]]
TestCase 2: 3,[[1,3],[2,3],[3,1]]
--TESTCASE END--
""" 
