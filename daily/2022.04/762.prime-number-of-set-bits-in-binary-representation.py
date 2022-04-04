"""
日期: 2022-04-05
题目: 二进制表示中质数个计算置位
链接: https://leetcode-cn.com/problems/prime-number-of-set-bits-in-binary-representation/
"""
class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        prime = set([2, 3, 5, 7, 11, 13, 17, 19])
        ans = 0
        for i in range(left, right + 1):
           if bin(i).count('1') in prime:
               ans += 1
        return ans
            