"""
日期: 2022-06-05
题目: 在圆内随机生成点
链接: https://leetcode-cn.com/problems/generate-random-point-in-a-circle/
"""

from typing import *
from collections import *
import random
class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.r = radius
        self.x = x_center
        self.y = y_center

    def randPoint(self) -> List[float]:
        while 1:
            x = random.uniform(-self.r, self.r)
            y = random.uniform(-self.r, self.r)
            if x * x + y * y <= self.r ** 2:
                break
        return [self.x + x, self.y + y]



# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()