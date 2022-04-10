"""
日期: 2022-04-11
题目: 统计各位数字都不同的数字个数
链接: https://leetcode-cn.com/problems/count-numbers-with-unique-digits/
"""
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        temp = [0 for _ in range(n + 1)]
        temp[0] = 1
        for i in range(1, n + 1):
            a = 1
            for j in range(i - 1):
                a *= (9 - j)
            temp[i] = temp[i - 1] + 9 * a
        return temp[-1]

