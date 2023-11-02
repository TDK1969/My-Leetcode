"""
日期: 2023-10-10
题目: 移动机器人
链接: https://leetcode-cn.com/problems/movement-of-robots/
"""

from typing import *
from collections import *
class Solution:
    def sumDistance(self, nums: List[int], s: str, d: int) -> int:
        mod = 10 ** 9 + 7
        pos = [nums[i] - d if s[i] == "L" else nums[i] + d for i in range(len(nums))]
        pos.sort()
        return sum([((pos[i] - pos[i - 1]) * i * (len(pos) - i)) % mod for i in range(1, len(pos))]) % mod