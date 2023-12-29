"""
日期: 2023-12-25
题目: 克隆图
链接: https://leetcode-cn.com/problems/clone-graph/
"""

from typing import *
from collections import *
from leetcode_utils import *

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        node_hash = dict()
        
        def dfs(ref_node: Optional['Node'], new_node: Optional['Node']):
            for neighbor in ref_node.neighbors:
                if neighbor.val not in node_hash:
                    new_neighbor_node = Node(neighbor.val)
                    node_hash[neighbor.val] = new_neighbor_node
                    dfs(neighbor, new_neighbor_node)
                else:
                    new_neighbor_node = node_hash[neighbor.val]
                new_node.neighbors.append(new_neighbor_node)
        
        new_node = Node(node.val)
        node_hash[node.val] = new_node
        dfs(node, new_node)
        return new_node
        


        

"""
--TESTCASE BEGIN--
TestCase 0: [[2,4],[1,3],[2,4],[1,3]]
TestCase 1: [[]]
TestCase 2: []
--TESTCASE END--
""" 
