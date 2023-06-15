"""
日期: 2023-02-03
题目: 二叉树着色游戏
链接: https://leetcode-cn.com/problems/binary-tree-coloring-game/
"""

from typing import *
from collections import *
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
        # turn tree to map
        if n == 1:
            return False
        m = defaultdict(list)
        q = deque()
        q.append(root)

        while q:
            t = q.popleft()
            if t.left:
                q.append(t.left)
                m[t.val].append(t.left.val)
                m[t.left.val].append(t.val)
            if t.right:
                q.append(t.right)
                m[t.val].append(t.right.val)
                m[t.right.val].append(t.val)
        
        def calc_score(s: int) -> int:
            q = deque()
            q.append(s)
            cnt = 1
            visited = set([x])

            while q:
                t = q.popleft()
                for nxt in m[t]:
                    if nxt not in visited:
                        q.append(nxt)
                        visited.add(nxt)
                        cnt += 1
            return cnt
        
        ans = [0, 0, 0]
        for i, nxt in enumerate(m[x]):
            ans[i] = calc_score(nxt)
        
        ans.sort()
        if ans[2] > ans[0] + ans[1] + 1:
            return True
        else:
            return False

node_index_list = [1,2,3,4,5,6,7,8,9,10,11]
node_list = [TreeNode(i) for i in node_index_list]
node_list[3].left = node_list[7]
node_list[3].right = node_list[8]
node_list[4].left = node_list[9]
node_list[4].right = node_list[10]
node_list[2].left = node_list[5]
node_list[2].right = node_list[6]
node_list[1].left = node_list[3]
node_list[1].right = node_list[4]
node_list[0].left = node_list[1]
node_list[0].right = node_list[2]
test = Solution()
print(test.btreeGameWinningMove(root = node_list[0], n = 11, x = 3))

            