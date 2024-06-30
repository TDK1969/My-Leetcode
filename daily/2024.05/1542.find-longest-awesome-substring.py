"""
日期: 2024-05-20
题目: 找出最长的超赞子字符串
链接: https://leetcode.cn/problems/find-longest-awesome-substring/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def longestAwesome(self, s: str) -> int:
        prefix = {0: -1}
        n = len(s)
        ans = 0
        seq = 0

        for i in range(n):
            digit = ord(s[i]) - 48
            seq = seq ^ (1 << digit)
            if seq in prefix:
                ans = max(ans, i - prefix[seq])
            else:
                prefix[seq] = i

            for k in range(10):
                if seq ^ (1 << k) in prefix:
                    ans = max(ans, i - prefix[seq ^ (1 << k)])
        return ans

            
print(Solution().longestAwesome("3242415"))
"""
--TESTCASE BEGIN--
TestCase 0: "3242415"
TestCase 1: "12345678"
TestCase 2: "213123"
--TESTCASE END--
""" 
