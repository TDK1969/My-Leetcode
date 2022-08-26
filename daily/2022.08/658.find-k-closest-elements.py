"""
日期: 2022-08-25
题目: 找到 K 个最接近的元素
链接: https://leetcode-cn.com/problems/find-k-closest-elements/
"""

from typing import *
from collections import *
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        return sorted(sorted(arr, key=lambda i:[abs(i - x), i])[:k])

t = Solution()
print(t.findClosestElements(arr = [1,2,3,4,5], k = 4, x = 3))