"""
题目: 移除指定数字得到的最大结果
链接: https://leetcode-cn.com/problems/remove-digit-from-number-to-maximize-result/
"""
class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        ans = 0
        for i in range(len(number)):
            num = number[i]
            if num == digit:
                temp = number[:i] + number[i + 1:]
                ans = max(ans, int(temp))
        return str(ans)
