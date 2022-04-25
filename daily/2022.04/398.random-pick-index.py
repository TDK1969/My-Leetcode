"""
日期: 2022-04-25
题目: 随机数索引
链接: https://leetcode-cn.com/problems/random-pick-index/
"""
import enum
from typing import List
from collections import defaultdict
import random

class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums


    def pick(self, target: int) -> int:
        ans = 0
        count = 0
        for index, num in enumerate(self.nums):
            if num == target:
                if random.randint(0, count) == 0:
                    ans = index
                count += 1
        return ans





# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)