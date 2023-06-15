"""
日期: 2023-02-12
题目: 字母板上的路径
链接: https://leetcode-cn.com/problems/alphabet-board-path/
"""

from typing import *
from collections import *
class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        ans = ""
        x = y = 0
        for alpha in target:
            nxt_x, nxt_y = (ord(alpha) - 97) // 5, (ord(alpha) - 97) % 5
            if nxt_y < y:
                ans += (y - nxt_y) * "L"
            if nxt_x < x:
                ans += (x - nxt_x) * "U"
            if nxt_x > x:
                ans += (nxt_x - x) * "D"
            if nxt_y > y:
                ans += (nxt_y - y) * "R"
                
            ans += "!"
            x, y = nxt_x, nxt_y
        return ans

test = Solution()
print(test.alphabetBoardPath("code"))