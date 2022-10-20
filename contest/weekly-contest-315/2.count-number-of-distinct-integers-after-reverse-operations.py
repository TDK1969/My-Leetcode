"""
题目: 反转之后不同整数的数目
链接: https://leetcode-cn.com/problems/count-number-of-distinct-integers-after-reverse-operations/
"""

from typing import *
from collections import *
class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        a = set(nums)
        for i in nums:
            a.add(int(str(i)[::-1]))
        return len(a)