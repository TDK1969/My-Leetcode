"""
日期: 2023-12-24
题目: 收集足够苹果的最小花园周长
链接: https://leetcode-cn.com/problems/minimum-garden-perimeter-to-collect-enough-apples/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        # 通过平方和公式推导,第k圈一共有2 * k * (k + 1) * (2k + 1)个苹果
        left = 1
        right = 100000
        while left < right:
            mid = (left + right) // 2
            if 2 * mid * (mid + 1) * (2 * mid + 1) >= neededApples:
                right = mid
            else:
                left = mid + 1
        
        return right * 8


"""
--TESTCASE BEGIN--
TestCase 0: 1
TestCase 1: 13
TestCase 2: 1000000000
--TESTCASE END--
""" 
print(Solution().minimumPerimeter(1000000000))