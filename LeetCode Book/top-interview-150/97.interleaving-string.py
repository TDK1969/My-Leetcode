"""
日期: 2024-03-20
题目: 交错字符串
链接: https://leetcode-cn.com/problems/interleaving-string/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n, m = len(s1), len(s2)
        if n + m != len(s3):
            return False
        dp = [False for _ in range(n + 1)]
        dp[0] = True
        for i in range(n):
            if dp[i] and s1[i] == s3[i]:
                dp[i + 1] = True
        
        for j in range(1, m + 1):
            dp[0] = dp[0] and s2[j - 1] == s3[j - 1]
            for i in range(1, n + 1):
                dp[i] = (s1[i - 1] == s3[i + j - 1] and dp[i - 1]) or (s2[j - 1] == s3[i + j - 1] and dp[i])
        
        return dp[-1]


print(Solution().isInterleave("","","d"))


"""
--TESTCASE BEGIN--
TestCase 0: "aabcc","dbbca","aadbbcbcac"
TestCase 1: "aabcc","dbbca","aadbbbaccc"
TestCase 2: "","",""
--TESTCASE END--
""" 
