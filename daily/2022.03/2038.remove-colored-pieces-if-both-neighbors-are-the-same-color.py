"""
题目: 如果相邻两个颜色均相同则删除当前颜色
链接: https://leetcode-cn.com/problems/remove-colored-pieces-if-both-neighbors-are-the-same-color/
"""
class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        AliceMoves = 0
        BobMoves = 0
        n = len(colors)

        for i in range(n - 2):
            if colors[i : i + 3] == "AAA":
                AliceMoves += 1
            if colors[i : i + 3] == "BBB":
                BobMoves += 1
        
        return AliceMoves > BobMoves

test = Solution()
print(test.winnerOfGame("AAAABBBB"))