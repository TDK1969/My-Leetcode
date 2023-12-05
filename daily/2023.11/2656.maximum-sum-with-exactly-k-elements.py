'''
Author: TDK 793065367@qq.com
Date: 2023-11-15 00:00:01
LastEditors: TDK 793065367@qq.com
LastEditTime: 2023-11-15 10:13:40
FilePath: /My-Leetcode/daily/2023.11/2656.maximum-sum-with-exactly-k-elements.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
"""
日期: 2023-11-15
题目: K 个元素的最大和
链接: https://leetcode-cn.com/problems/maximum-sum-with-exactly-k-elements/
"""

from typing import *
from collections import *
class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        return (2 * max(nums) + k - 1) * k // 2