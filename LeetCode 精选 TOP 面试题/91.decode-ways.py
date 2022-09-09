"""
日期: 2022-07-14
题目: 解码方法
链接: https://leetcode-cn.com/problems/decode-ways/
"""

from typing import *
from collections import *
class Solution:
    def numDecodings(self, s: str) -> int:
        # 有前导零直接返回0
        if s[0] == '0':
            return 0
        n = len(s)
        # dp数组为n+1，需要增加一位空字符
        dp = [0 for _ in range(n + 1)]
        dp[0] = 1
        # 因为排除了前导0,所以第一个数字一定可行
        dp[1] = 1
        for j in range(2, n + 1):
            i = j - 1
            # 单个数字,只要不是0就可行
            if s[i] != '0':
                dp[j] += dp[j - 1]
            # 连续两个数字,第一位是1或第一位是2且第二位在1到6
            if s[i - 1] == '1' or s[i - 1] == '2' and '0' <= s[i] <= '6':
                dp[j] += dp[j - 2]
        return dp[-1]

test = Solution()
print(test.numDecodings("11106"))
