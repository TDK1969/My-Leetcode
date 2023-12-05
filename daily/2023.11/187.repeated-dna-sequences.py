"""
日期: 2023-11-05
题目: 重复的DNA序列
链接: https://leetcode-cn.com/problems/repeated-dna-sequences/
"""

from typing import *
from collections import *
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        ans = set()
        visited = set()
        for i in range(len(s) - 9):
            if s[i:i + 10] in visited:
                ans.add(s[i:i + 10])
            visited.add(s[i:i + 10])
        return list(ans)

print(Solution().findRepeatedDnaSequences("AAAAAAAAAAA"))