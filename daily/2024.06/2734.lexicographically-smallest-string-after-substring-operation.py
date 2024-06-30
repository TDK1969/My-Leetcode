"""
日期: 2024-06-27
题目: 执行子串操作后的字典序最小字符串
链接: https://leetcode.cn/problems/lexicographically-smallest-string-after-substring-operation/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def smallestString(self, s: str) -> str:
        n = len(s)
        ans = ""
        flag = 0
        for i in range(n):
            if s[i] != "a":
                if flag == 0 or flag == 1:
                    ans += chr((ord(s[i]) - 98) % 26 + 97)
                    flag = 1
                else:
                    ans += s[i]
            else:
                if flag == 1:
                    flag = 2
                ans += s[i]
        
        if flag == 0:
            ans = ans[:-1] + "z"
        
        return ans

print(Solution().smallestString("aa"))



"""
--TESTCASE BEGIN--
TestCase 0: "cbabc"
TestCase 1: "aa"
TestCase 2: "acbbc"
TestCase 3: "leetcode"
--TESTCASE END--
""" 
