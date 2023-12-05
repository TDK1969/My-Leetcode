"""
日期: 2023-11-29
题目: 无限集中的最小数字
链接: https://leetcode-cn.com/problems/smallest-number-in-infinite-set/
"""

from typing import *
from collections import *
from leetcode_utils import *
class SmallestInfiniteSet:

    def __init__(self):
        self.removed_set = set()
        self.smallest_num = 1


    def popSmallest(self) -> int:
        ans = self.smallest_num
        self.removed_set.add(self.smallest_num)
        while self.smallest_num in self.removed_set:
            self.smallest_num += 1
        return ans


    def addBack(self, num: int) -> None:
        if num in self.removed_set:
            self.removed_set.remove(num)
        if num < self.smallest_num:
            self.smallest_num = num
        elif num == self.smallest_num:
            self.smallest_num = 1
            while self.smallest_num in self.removed_set:
                self.smallest_num += 1



# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)

"""
--TESTCASE BEGIN--
TestCase 0: ["SmallestInfiniteSet","addBack","popSmallest","popSmallest","popSmallest","addBack","popSmallest","popSmallest","popSmallest"],[[],[2],[],[],[],[1],[],[],[]]
--TESTCASE END--
""" 
