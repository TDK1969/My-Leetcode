"""
日期: 2022-12-13
题目: 判断句子是否为全字母句
链接: https://leetcode-cn.com/problems/check-if-the-sentence-is-pangram/
"""

from typing import *
from collections import *
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set(sentence)) == 26

test = Solution()
print(test.checkIfPangram('thequickbrownfoxjumpsoverthelazydog'))