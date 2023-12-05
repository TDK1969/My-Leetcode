"""
日期: 2023-11-23
题目: HTML 实体解析器
链接: https://leetcode-cn.com/problems/html-entity-parser/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def entityParser(self, text: str) -> str:

"""
--TESTCASE BEGIN--
TestCase 0: "&amp; is an HTML entity but &ambassador; is not."
TestCase 1: "and I quote: &quot;...&quot;"
--TESTCASE END--
""" 
