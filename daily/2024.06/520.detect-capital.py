"""
日期: 2024-06-23
题目: 检测大写字母
链接: https://leetcode.cn/problems/detect-capital/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        # code = 0b000
        # 00 - 初始化，01-存在小写字母，01-存在大写字母，11-同时大写小写
        code = 0
        if 65 <= ord(word[0]) <= 90:
            code |= 4
        n = len(word)
        for i in range(1, n):
            if 65 <= ord(word[i]) <= 90:
                code |= 2
            else:
                code |= 1
        # 非法：0b111, 0b011, 0b010
        if code == 7 or code == 3 or code == 2:
            return False
        return True
            
print(Solution().detectCapitalUse("AA"))     

"""
--TESTCASE BEGIN--
TestCase 0: "USA"
TestCase 1: "FlaG"
--TESTCASE END--
""" 
