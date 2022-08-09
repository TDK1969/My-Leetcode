"""
题目: 受限条件下可到达节点的数目
链接: https://leetcode-cn.com/problems/reachable-nodes-with-restrictions/
"""

from typing import *
from collections import *

class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        restricted = set(restricted)
        visited = set()
        tree_map = defaultdict(list)
        for node1, node2 in edges:
            tree_map[node1].append(node2)
            tree_map[node2].append(node1)
        
        ans = 1
        q = deque()
        q.append(0)
        visited.add(0)

        while q:
            t = q.popleft()
            for nxt_node in tree_map[t]:
                if nxt_node not in restricted and nxt_node not in visited:
                    ans += 1
                    q.append(nxt_node)
                    visited.add(nxt_node)
        
        return ans
            
