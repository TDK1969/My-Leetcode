"""
题目: 重排字符形成目标字符串
链接: https://leetcode-cn.com/problems/rearrange-characters-to-make-target-string/
"""

from typing import *
from collections import *
class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        c1 = Counter(s)
        c2 = Counter(target)
        ans = float("inf")
        for t in target:
            ans = min(ans, c1[t] // c2[t])
        return ans

test = Solution()
print(test.rearrangeCharacters("codecodecodecode", "codecode"))