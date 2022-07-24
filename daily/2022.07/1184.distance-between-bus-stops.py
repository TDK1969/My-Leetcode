"""
日期: 2022-07-24
题目: 公交站间的距离
链接: https://leetcode-cn.com/problems/distance-between-bus-stops/
"""

from typing import *
from collections import *
class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        return min(sum(distance[min(start, destination):max(start, destination)]), sum(distance) - sum(distance[min(start, destination):max(start, destination)]))


