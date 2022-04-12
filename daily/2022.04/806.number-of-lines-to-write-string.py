"""
日期: 2022-04-12
题目: 写字符串需要的行数
链接: https://leetcode-cn.com/problems/number-of-lines-to-write-string/
"""
from typing import List


class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        lines = 1
        blocks = 0

        for letter in s:
            if blocks + widths[ord(letter) - 97] > 100:
                lines += 1
                blocks = 0
            blocks += widths[ord(letter) - 97]
        
        return [lines, blocks]
