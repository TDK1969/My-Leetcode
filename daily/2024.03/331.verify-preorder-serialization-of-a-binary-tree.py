"""
日期: 2024-03-31
题目: 验证二叉树的前序序列化
链接: https://leetcode.cn/problems/verify-preorder-serialization-of-a-binary-tree/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:

"""
--TESTCASE BEGIN--
TestCase 0: "9,3,4,#,#,1,#,#,2,#,6,#,#"
TestCase 1: "1,#"
TestCase 2: "9,#,#,1"
--TESTCASE END--
""" 
