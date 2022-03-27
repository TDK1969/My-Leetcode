"""
日期: 2022-03-27
题目: 找出缺失的观测数据
链接: https://leetcode-cn.com/problems/find-missing-observations/
"""
from typing import List


class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        mSum = sum(rolls)
        nSum = mean * (m + n) - mSum
        if nSum > 6 * n or nSum < n:
            return []
        
        k = nSum // n
        x = (k + 1) * n - nSum
        return [k] * x + [k + 1] * (n - x)




