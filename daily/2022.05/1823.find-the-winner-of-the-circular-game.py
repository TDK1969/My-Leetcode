"""
日期: 2022-05-04
题目: 找出游戏的获胜者
链接: https://leetcode-cn.com/problems/find-the-winner-of-the-circular-game/
"""

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        """
        从最终状态倒推约瑟夫环
        """
        pos = 0
        cnt = 1
        while cnt <= n:
            pos = (pos + k) % cnt
            cnt += 1
        return pos + 1

test = Solution()
print(test.findTheWinner(n = 5, k = 2))

