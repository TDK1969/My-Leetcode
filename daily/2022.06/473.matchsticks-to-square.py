"""
日期: 2022-06-01
题目: 火柴拼正方形
链接: https://leetcode-cn.com/problems/matchsticks-to-square/
"""

from typing import *
from collections import *

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        length_sum = sum(matchsticks)
        if length_sum & 3 != 0:
            return False
        length = length_sum // 4
        matchsticks.sort(reverse=True)
    
        dp = [-1 for _ in range(1 << len(matchsticks))]
        dp[0] = 0
        
        for i in range(1, len(dp)):
            # 遍历状态i的所有前一个状态
            for k, v in enumerate(matchsticks):
                if i & (1 << k) == 0:
                    continue
                s = i & ~(1 << k)
                if dp[s] >= 0 and dp[s] + v <= length:
                    dp[i] = (dp[s] + v) % length
                    break
        return dp[-1] == 0

test = Solution()
print(test.makesquare(matchsticks = [1,1,2,2,2]))
        

                




