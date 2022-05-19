"""
日期: 2022-05-18
题目: 乘法表中第k小的数
链接: https://leetcode-cn.com/problems/kth-smallest-number-in-multiplication-table/
"""

from typing import *
from collections import *
class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        if k == 1:
            return 1
        if k == m * n:
            return m * n

        def judge(num: int) -> bool:
            temp = 0
            for i in range(1, m + 1):
                temp += min(n, num // i)
            return temp < k
        
        left = 1
        right = m * n

        while left < right:
            mid = (left + right) // 2
            if judge(mid):
                left = mid + 1
            else:
                right = mid
        return left


        
#[1 ~ m * n] 二分法
# 给定一个数num,如何判断num的排序