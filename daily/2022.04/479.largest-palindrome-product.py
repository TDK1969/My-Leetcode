"""
日期: 2022-04-16
题目: 最大回文数乘积
链接: https://leetcode-cn.com/problems/largest-palindrome-product/
"""
class Solution:
    def largestPalindrome(self, n: int) -> int:
        if n == 1:
            return 9
        for i in range(10 ** n - 1, 10 ** (n - 1), -1):
            p = int(str(i) + str(i)[::-1])
            for x in range(10 ** n - 1, 10 ** (n - 1), -1):
                if x * x < p:
                    break
                if p % x == 0 and len(str(p // x)) == n:
                    return p % 1337

test = Solution()

ans = []
for i in range(1, 9):
    ans.append(test.largestPalindrome(i))
print(ans)