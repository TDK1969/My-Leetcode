"""
日期: 2022-03-26
题目: 棒球比赛
链接: https://leetcode-cn.com/problems/baseball-game/
"""
from typing import List


class Solution:
    def calPoints(self, ops: List[str]) -> int:
        records = []

        for op in ops:
            if op == "+":
                records.append(records[-1] + records[-2])
            elif op == "D":
                records.append(records[-1] * 2)
            elif op == "C":
                records.pop()
            else:
                records.append(int(op))
        
        return sum(records)