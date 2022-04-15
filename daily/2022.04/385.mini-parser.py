"""
日期: 2022-04-15
题目: 迷你语法分析器
链接: https://leetcode-cn.com/problems/mini-parser/
"""
from typing import List, Union


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
    def __init__(self, value=None):
        """
        If value is not specified, initializes an empty list.
        Otherwise initializes a single integer equal to value.
        """

    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """

    def add(self, elem):
        """
        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
        :rtype void
        """

    def setInteger(self, value):
        """
        Set this NestedInteger to hold a single integer equal to value.
        :rtype void
        """

    def getInteger(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """

    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """
class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        if not s:
            return NestedInteger()
        if s[0] != "[":
            return NestedInteger(int(s))
        if len(s) <= 2:
            return NestedInteger()
        
        res = NestedInteger()

        start, level, end = 1, 0, len(s)

        for i in range(1, end):
            if level == 0 and (s[i] == "," or i == end - 1):
                # 在本次递归中的每一项
                res.add(self.deserialize(s[start:i]))
                start = i + 1
            elif s[i] == "[":
                level += 1
            elif s[i] == "]":
                level -= 1
        return res

                

