"""
日期: 2023-06-07
题目: 老鼠和奶酪
链接: https://leetcode-cn.com/problems/mice-and-cheese/
"""

from typing import *
from collections import *
class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        n = len(reward1)
        cheese = sorted([i for i in range(n)], key=lambda x:(reward1[x] - reward2[x]), reverse=True)
        ans = 0
        for i in range(n):
            if i < k:
                ans += reward1[cheese[i]]
            else:
                ans += reward2[cheese[i]]
        return ans
    
test = Solution()
print(test.miceAndCheese(reward1 = [1,1,3,4], reward2 = [4,4,1,1], k = 2))
