"""
日期: 2022-03-28
题目: 交替位二进制数
链接: https://leetcode-cn.com/problems/binary-number-with-alternating-bits/
"""
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        bit = n & 1
        n = n >> 1

        while n:
            temp = n & 1
            if temp == bit:
                return False
            else:
                bit = temp
                n = n >> 1
        
        return True