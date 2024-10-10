"""
日期: 2024-09-19
题目: 最长的字母序连续子字符串的长度
链接: https://leetcode.cn/problems/length-of-the-longest-alphabetical-continuous-substring/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        ans = 1
        cur = 1
        pre = s[0]
        n = len(s)
        for i in range(1, n):
            if ord(s[i]) == ord(pre) + 1:
                cur += 1
            else:
                if cur > ans:
                    ans = cur
                cur = 1
            pre = s[i]
        if cur > ans:
            ans = cur
        
        return ans

print(Solution().longestContinuousSubstring("abcde"))

        
            

"""
--TESTCASE BEGIN--
TestCase 0: "abacaba"
TestCase 1: "abcde"
--TESTCASE END--
""" 
