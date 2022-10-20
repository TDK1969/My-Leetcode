"""
日期: 2022-09-13
题目: 最大交换
链接: https://leetcode-cn.com/problems/maximum-swap/
"""

from typing import *
from collections import *
class Solution:
    def maximumSwap(self, num: int) -> int:
        k = num
        a = []
        while k:
            a.append(k % 10)
            k = k // 10
        a.reverse()
        n = len(a)

        right_max = [0 for _ in range(n)]
        right_max[-1] = n - 1
        for i in range(n - 2, -1, -1):
            if a[i] > a[right_max[i + 1]]:
                right_max[i] = i
            else:
                right_max[i] = right_max[i + 1]
            

        for i in range(n):
            if i != right_max[i] and a[i] != a[right_max[i]]:
                a[i], a[right_max[i]] = a[right_max[i]], a[i]
                break
        ans = 0
        for i in range(n):
            ans = ans * 10 + a[i]
        
        return ans
test = Solution()
print(test.maximumSwap(2088))



