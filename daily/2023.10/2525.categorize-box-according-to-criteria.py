"""
日期: 2023-10-20
题目: 根据规则将箱子分类
链接: https://leetcode-cn.com/problems/categorize-box-according-to-criteria/
"""

from typing import *
from collections import *
class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        bulky = max(length, width, height) >= 10 ** 4 or length * width * height >= 10 ** 9
        heavy = mass >= 100
        if bulky and heavy:
            return "Both"
        if bulky and not heavy:
            return "Bulky"
        if heavy and not bulky:
            return "Heavy"
        else:
            return "Neither"