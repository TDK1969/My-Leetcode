"""
日期: 2025-01-01
题目: 将日期转换为二进制表示
链接: https://leetcode.cn/problems/convert-date-to-binary/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def convertDateToBinary(self, date: str) -> str:
        arr = list(map(int, date.split("-")))

        return f"{arr[0]:b}-{arr[1]:b}-{arr[2]:b}"
        

print(Solution().convertDateToBinary("2080-02-29"))
"""
--TESTCASE BEGIN--
TestCase 0: "2080-02-29"
TestCase 1: "1900-01-01"
--TESTCASE END--
""" 
