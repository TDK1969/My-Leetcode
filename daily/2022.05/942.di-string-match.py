"""
日期: 2022-05-09
题目: 增减字符串匹配
链接: https://leetcode-cn.com/problems/di-string-match/
"""

from typing import *
from collections import *
class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        ans = [0]
        top = 0
        down = 0

        for i in s:
            if i == "I":
                top += 1
                ans.append(top)
            if i == "D":
                down += 1
                ans.append(-down)
        
        for j in range(len(ans)):
            ans[j] += down
        
        return ans