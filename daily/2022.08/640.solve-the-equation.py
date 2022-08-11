"""
日期: 2022-08-10
题目: 求解方程
链接: https://leetcode-cn.com/problems/solve-the-equation/
"""

from typing import *
from collections import *
class Solution:
    def solveEquation(self, equation: str) -> str:
        factor = val = 0
        i, n, sign = 0, len(equation), 1  # 等式左边默认系数为正
        while i < n:
            if equation[i] == '=':
                sign = -1
                i += 1
                continue

            s = sign
            if equation[i] == '+':  # 去掉前面的符号
                i += 1
            elif equation[i] == '-':
                s = -s
                i += 1

            num, valid = 0, False
            while i < n and equation[i].isdigit():
                valid = True
                num = num * 10 + int(equation[i])
                i += 1

            if i < n and equation[i] == 'x':  # 变量
                factor += s * num if valid else s
                i += 1
            else:  # 数值
                val += s * num

        if factor == 0:
            return "No solution" if val else "Infinite solutions"
        return f"x={-val // factor}"