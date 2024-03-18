"""
日期: 2022-07-14
题目: 最长公共前缀
链接: https://leetcode-cn.com/problems/longest-common-prefix/
"""

from typing import *
from collections import *
class Solution:
    def longestCommonPrefix(self, s: List[str]) -> str:
        if not s:
            return ""
        ans = s[0]
        for ss in s[1:]:
            while ss.find(ans) != 0:
                ans = ans[:len(ans) - 1]
        return ans


test = Solution()
print(test.longestCommonPrefix(["dog","racecar","car"]))

