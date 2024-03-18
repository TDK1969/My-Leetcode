"""
日期: 2024-01-19
题目: 二进制求和
链接: https://leetcode-cn.com/problems/add-binary/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_bin = int(a, 2)
        b_bin = int(b, 2)
        return bin(a_bin + b_bin)[2:]

print(Solution().addBinary("1010","1011"))
"""
--TESTCASE BEGIN--
TestCase 0: "11","1"
TestCase 1: "1010","1011"
--TESTCASE END--
""" 
