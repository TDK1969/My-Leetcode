"""
日期: 2022-04-14
题目: 最富有客户的资产总量
链接: https://leetcode-cn.com/problems/richest-customer-wealth/
"""
from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max([sum(i) for i in accounts])