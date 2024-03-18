"""
日期: 2023-11-01
题目: 验证回文串
链接: https://leetcode-cn.com/problems/valid-palindrome/
"""

from typing import *
from collections import *
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l <= r:
            while l < len(s) and not s[l].isalnum():
                l += 1
            while r >= 0 and not s[r].isalnum():
                r -= 1
            if l <= r and s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True

print(Solution().isPalindrome("A man, a plan, a canal: Panama"))