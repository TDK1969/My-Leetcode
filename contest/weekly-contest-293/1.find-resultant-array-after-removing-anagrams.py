"""
题目: 移除字母异位词后的结果数组
链接: https://leetcode-cn.com/problems/find-resultant-array-after-removing-anagrams/
"""

from typing import *
from collections import *
class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        ans = [words[0]]
        n = len(words)
        i = 1

        while i < n:
            if sorted(words[i]) == sorted(ans[-1]):
                i += 1
            else:
                ans.append(words[i])
        return ans