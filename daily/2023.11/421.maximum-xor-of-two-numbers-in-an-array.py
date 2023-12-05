"""
日期: 2023-11-04
题目: 数组中两个数的最大异或值
链接: https://leetcode-cn.com/problems/maximum-xor-of-two-numbers-in-an-array/
"""

from typing import *
from collections import *
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        pre_set = [set() for _ in range(32)]

        for num in nums:
            for i in range(32):
                pre_set[i].add(num >> (31 - i))
        
        ans = 0
        for i in range(32):
            # 假设第31 - i位能够达到1
            ans <<= 1
            ans += 1
            flag = False
            for pre in pre_set[i]:
                if ans ^ pre in pre_set[i]:
                    flag = True
                    break
            if not flag:
                ans -= 1
        
        return ans

print(Solution().findMaximumXOR([1]))