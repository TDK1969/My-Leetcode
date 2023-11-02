"""
日期: 2023-10-26
题目: 加油站
链接: https://leetcode-cn.com/problems/gas-station/
"""

from typing import *
from collections import *
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        ans = -1
        remain = 0
        presum = 0
        
        for i in range(n):
            presum += gas[i] - cost[i]
            if remain + gas[i] - cost[i] < 0:
                ans = -1
                remain = 0
            else:
                if ans == -1:
                    ans = i
                remain += gas[i] - cost[i]

        return ans if presum >= 0 else -1
    
print(Solution().canCompleteCircuit(gas = [1,2,3,4,5], cost = [3,4,5,1,2]))