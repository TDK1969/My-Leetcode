"""
日期: 2024-08-06
题目: 找出所有稳定的二进制数组 I
链接: https://leetcode.cn/problems/find-all-possible-stable-binary-arrays-i/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:

"""
--TESTCASE BEGIN--
TestCase 0: 1,1,2
TestCase 1: 1,2,1
TestCase 2: 3,3,2
--TESTCASE END--
""" 
