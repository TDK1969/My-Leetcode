"""
日期: 2022-08-14
题目: 分割字符串的最大得分
链接: https://leetcode-cn.com/problems/maximum-score-after-splitting-a-string/
"""

from typing import *
from collections import *
class Solution:
    def maxScore(self, s: str) -> int:
        t = [0]
        for i in s:
            t.append(t[-1] + (1 if i == "1" else 0))
        
        ans = 0
        # i 为 左子字符串的长度
        for i in range(1, len(s)):
            ans = max(ans, i - t[i] + t[-1] - t[i])
        return ans
test = Solution()
print(test.maxScore(s = "011101"))


