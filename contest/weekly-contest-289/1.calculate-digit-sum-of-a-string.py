"""
题目: 计算字符串的数字和
链接: https://leetcode-cn.com/problems/calculate-digit-sum-of-a-string/
"""
class Solution:
    def digitSum(self, s: str, k: int) -> str:
        ans = s
        while len(ans) > k:
            temp = ""
            for i in range(0, len(ans), k):
                a = int(ans[i : i + k])
                b = 0
                while a:
                    b += a % 10
                    a = a // 10
                temp += str(b)
            ans = temp
        return ans