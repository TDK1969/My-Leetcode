"""
日期: 2022-07-14
题目: 加一
链接: https://leetcode-cn.com/problems/plus-one/
"""

from typing import *
from collections import *
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans = digits[::-1]
        flag = 1
        n = len(ans)
        for i in range(n):
            t = flag + ans[i]
            ans[i] = t % 10
            flag = t // 10
        if flag:
            ans.append(1)
        return ans[::-1]
        