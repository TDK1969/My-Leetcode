"""
日期: 2022-04-18
题目: 字典序排数
链接: https://leetcode-cn.com/problems/lexicographical-numbers/
"""
from typing import List


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ans = [0 for _ in range(n)]
        cur = 1
        # 思路类似深度优先搜索
        for i in range(n):
            ans[i] = cur
            if cur * 10 <= n:
                cur *= 10
            else:
                if cur >= n:
                    cur //= 10
                cur += 1
                while cur % 10 == 0:
                    cur //= 10
        return ans

            

test = Solution()
print(test.lexicalOrder(35))