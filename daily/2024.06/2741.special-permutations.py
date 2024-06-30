"""
日期: 2024-06-26
题目: 特别的排列
链接: https://leetcode.cn/problems/special-permutations/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        mod = 10 ** 9 + 7
        n = len(nums)
        # 状态压缩 state >> i & 1 == 1 表示为1表示排列中有第i个数
        # dp[state][i]表示在排列为state且最后一个数为nums[i]时排列的总数目
        dp = [[0 for _ in range(n)] for _ in range(1 << n)]

        # 初始化，只选择第i个数时，排列数目为1
        for i in range(n):
            dp[1 << i][i] = 1
        
        # 开始dp
        for state in range(1, 1 << n):
            # 枚举存在于当前排列state中的数
            for i, x in enumerate(nums):
                # 如果第i个数不存在于当前排列中，continue
                if not state >> i & 1:
                    continue

                # 枚举state中除第i个数以外的数
                for j, y in enumerate(nums):
                    if i == j or not state >> j & 1:
                        continue
                    # 如果最后一位不满足整除的条件，continue
                    if x % y != 0 and y % x != 0:
                        continue
                    # state ^ (1 << i) 表示将第i位置为0，即第i个数不存在state时的排列
                    # dp[state ^ (1 << i)][j] 表示第i个数不存在state时的排列且以第j个数作为结尾
                    dp[state][i] = (dp[state][i] + dp[state ^ (1 << i)][j]) % mod
        
        return sum([dp[(1 << n) - 1][i] for i in range(n)]) % mod

print(Solution().specialPerm([2,3,6]))


"""
--TESTCASE BEGIN--
TestCase 0: [2,3,6]
TestCase 1: [1,4,3]
--TESTCASE END--
""" 
