"""
日期: 2024-10-16
题目: 最小元素和最大元素的最小平均值
链接: https://leetcode.cn/problems/minimum-average-of-smallest-and-largest-elements/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        cnt = [0 for _ in range(51)]
        for num in nums:
            cnt[num] += 1
        res = []
        for i, c in enumerate(cnt):
            for _ in range(c):
                res.append(i)

        #nums.sort()
        n = len(nums)
        i, j = 0, n - 1
        ans = float("inf")
        while i < j:
            ans = min(ans, res[i] + res[j])
            i += 1
            j -= 1
        return ans / 2

print(Solution().minimumAverage([7,8,3,4,15,13,4,1]))



"""
--TESTCASE BEGIN--
TestCase 0: [7,8,3,4,15,13,4,1]
TestCase 1: [1,9,8,3,10,5]
TestCase 2: [1,2,3,7,8,9]
--TESTCASE END--
""" 
