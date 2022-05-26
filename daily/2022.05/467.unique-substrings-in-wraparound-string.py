"""
日期: 2022-05-25
题目: 环绕字符串中唯一的子字符串
链接: https://leetcode-cn.com/problems/unique-substrings-in-wraparound-string/
"""

from typing import *
from collections import *
class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        n = len(p)
        left = 0 
        right = 1
        dp = defaultdict(int)

        while right < n:
            if ord(p[right]) == ord(p[right - 1]) + 1 or p[right - 1] == "z" and p[right] == "a":
                dp[p[right - 1]] = max(dp[p[right - 1]], right - left)
                right += 1
            else:
                dp[p[right - 1]] = max(dp[p[right - 1]], right - left)
                left = right
                right += 1
        
        dp[p[right - 1]] = max(dp[p[right - 1]], right - left)
        return sum(dp.values())

test = Solution()
print(test.findSubstringInWraproundString("zaba"))
        
        