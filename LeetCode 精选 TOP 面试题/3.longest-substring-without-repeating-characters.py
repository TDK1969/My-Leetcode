"""
日期: 2022-07-14
题目: 无重复字符的最长子串
链接: https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/
"""

from typing import *
from collections import *
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = set()
        left, right = 0, 0
        ans = 1
        n = len(s)
        while left < n and right < n:
            if s[right] not in visited:
                visited.add(s[right])
                right += 1
                ans = max(ans, right - left)
            else:
                visited.remove(visited[left])
                left += 1
        return ans