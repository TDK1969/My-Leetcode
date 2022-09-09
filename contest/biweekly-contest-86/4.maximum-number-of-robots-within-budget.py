"""
题目: 预算内的最多机器人数目
链接: https://leetcode-cn.com/problems/maximum-number-of-robots-within-budget/
"""

from typing import *
from collections import *

class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        n = len(chargeTimes)
        index = [i for i in range(n)]
        def min_K_cost(k: int) -> int:
            index.sort(key=lambda x:k * runningCosts[x] + chargeTimes[x] / k)
            cost = 0
            max_charge_time = 0
            for i in index[:k]:
                max_charge_time = max(max_charge_time, chargeTimes[i])
                cost += k * runningCosts[i]
            cost += max_charge_time
            return cost
        
        left = 0
        right = n
        while left < right:
            mid = (left + right) // 2
            if min_K_cost(mid) > budget:
                right = mid
            else:
                left = mid + 1
        return right

test = Solution()
print(test.maximumRobots([11,12,74,67,37,87,42,34,18,90,36,28,34,20],[18,98,2,84,7,57,54,65,59,91,7,23,94,20]
,937))

            