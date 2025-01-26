"""
日期: 2024-10-25
题目: 执行操作可获得的最大总奖励 I
链接: https://leetcode.cn/problems/maximum-total-reward-using-operations-i/
"""

from typing import *
from collections import *
from leetcode_utils import *
import heapq
class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        rewardValues.sort()
        dp = set()

        dp.add(0)
    
        for reward in rewardValues:
            tmp = set()
            for k in dp:
                if reward > k:
                    tmp.add(k + reward)
            dp.update(tmp)
        
        return max(dp)

            
print(Solution().maxTotalReward([6,13,9,19]))


        

"""
--TESTCASE BEGIN--
TestCase 0: [1,1,3,3]
TestCase 1: [1,6,4,3,2]
--TESTCASE END--
""" 
