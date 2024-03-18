"""
日期: 2024-03-07
题目: 单词拆分
链接: https://leetcode-cn.com/problems/word-break/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        wordSet = set(wordDict)
        dp = [False for _ in range(n + 1)]
        dp[0] = True
        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True
                    break
        return dp[-1]

print(Solution().wordBreak("applepenapple",["apple","pen"]))
"""
--TESTCASE BEGIN--
TestCase 0: "leetcode",["leet","code"]
TestCase 1: "applepenapple",["apple","pen"]
TestCase 2: "catsandog",["cats","dog","sand","and","cat"]
--TESTCASE END--
""" 
