"""
日期: 2022-07-04
题目: 最小绝对差
链接: https://leetcode-cn.com/problems/minimum-absolute-difference/
"""

from typing import *
from collections import *
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        ans = []
        n = len(arr)
        m = float("inf")
        for i in range(1, n):
            if arr[i] - arr[i - 1] < m:
                ans = [[arr[i - 1], arr[i]]]
                m = arr[i] - arr[i - 1]
            elif arr[i] - arr[i - 1] == m:
                ans.append([arr[i - 1], arr[i]])
        return ans
