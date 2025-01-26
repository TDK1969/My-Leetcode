"""
日期: 2025-01-19
题目: 统计打字方案数
链接: https://leetcode.cn/problems/count-number-of-texts/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        n = len(pressedKeys)
        dp = [0 for _ in range(n + 1)]
        dp[0] = 0
        dp[1] = 1
        buttoms = {
            '2': 3,
            '3': 3,
            '4': 3,
            '5': 3,
            '6': 3,
            '7': 4,
            '8': 3,
            '9': 4
        }
        mod = 10 ** 9 + 7

        for i in range(1, n):
            k = i + 1
            if pressedKeys[i] == pressedKeys[i - 1]:
                if pressedKeys[i] == '7' or pressedKeys[i] == '9':
                    t = 4
                else:
                    t = 3
                




        

"""
--TESTCASE BEGIN--
TestCase 0: "22233"
TestCase 1: "222222222222222222222222222222222222"
--TESTCASE END--
""" 
