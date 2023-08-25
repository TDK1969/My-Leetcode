"""
日期: 2023-06-19
题目: 可被三整除的最大和
链接: https://leetcode-cn.com/problems/greatest-sum-divisible-by-three/
vscode://vscode-remote/ssh-remote+www.mdecade.site/home/tdk/Study/My-Leetcode/daily/2023.06/1262.greatest-sum-divisible-by-three.py
"""

from typing import *
from collections import *
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        # 贪心的做法
        nums.sort()
        # 先对数组排序
        res = sum(nums)
        s = [[] for _ in range(3)]
        for num in nums:
            s[num % 3].append(num)
        
        if res % 3 == 0:
            return res
        else:
            # 如果和不能被3整除,则减去最小的部分使可以被整除
            k = res % 3
            return max(res - s[k][0] if len(s[k]) >= 1 else 0, res - s[3 - k][0] - s[3 - k][1] if len(s[3 - k]) >= 2 else 0)
        
        
