"""
日期: 2024-07-15
题目: 账户合并
链接: https://leetcode.cn/problems/accounts-merge/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

"""
--TESTCASE BEGIN--
TestCase 0: [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
TestCase 1: [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]
--TESTCASE END--
""" 
