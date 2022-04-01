"""
日期: 2022-03-31
题目: 自除数
链接: https://leetcode-cn.com/problems/self-dividing-numbers/
"""
from typing import List


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []
        for num in range(left, right + 1):
            i = num
            flag = True
            while i:
                if i % 10 == 0 or num % (i % 10) != 0:
                    flag = False
                    break
                i = i // 10
            if flag:
                ans.append(num)
        return ans