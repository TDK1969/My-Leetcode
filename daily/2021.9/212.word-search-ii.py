from typing import List
from collections import defaultdict
class DictTree:
    def __init__(self):
        self.is_word = False
        self.children = defaultdict(DictTree)
        self.word = ""

    def insert(self, word: str):
        cur = self
        for c in word:
            cur = cur.children[c]
        cur.is_word = True
        cur.word = word


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = DictTree()
        for word in words:
            root.insert(word)

        m = len(board)
        n = len(board[0])
        ans = set()

        def dfs(now: DictTree, x: int, y: int):
            char = board[x][y]
            if char not in now.children:
                return

            now = now.children[char]
            if now.is_word:
                ans.add(now.word)

            board[x][y] = '#'
            for d_x, d_y in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                if 0 <= x + d_x < m and 0 <= y + d_y < n:
                    dfs(now, x + d_x, y + d_y)
            board[x][y] = char

        for i in range(m):
            for j in range(n):
                dfs(root, i, j)

        return list(ans)

test = Solution()
print(test.findWords(board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]))

