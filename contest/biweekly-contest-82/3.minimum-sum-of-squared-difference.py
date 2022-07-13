"""
题目: 最小差值平方和
链接: https://leetcode-cn.com/problems/minimum-sum-of-squared-difference/
"""

import heapq
from typing import *
from collections import *

class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:

        t = [0] * (10 ** 5 + 5)
        # t[i] = j 表示绝对值为i有j个
        max_abs = -1
        for n1, n2 in zip(nums1, nums2):
            max_abs = max(j, abs(n1 - n2))
            t[abs(n1 - n2)] += 1
        
        k = k1 + k2
        j = max_abs
        while j > 0 and k > 0:
            # 逐级减少
            c = min(k, t[j])
            t[j] -= c
            k -= c
            t[j - 1] += c
            j -= 1
        
        ans = 0
        for i in range(max_abs + 1):
            ans += t[i] * i * i
        return ans



