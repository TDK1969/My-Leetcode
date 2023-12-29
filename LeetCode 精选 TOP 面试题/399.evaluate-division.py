"""
日期: 2023-12-25
题目: 除法求值
链接: https://leetcode-cn.com/problems/evaluate-division/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Node:
    def __init__(self, name: str):
        self.name = name
        self.neighbors: Dict[str, Node] = {}
        

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        hash_node : Dict[str, Node]= dict()
        for i in range(len(equations)):
            x, y = equations[i]
            if x not in hash_node:
                x_node = Node(x)
                hash_node[x] = x_node
            x_node = hash_node[x]

            if y not in hash_node:
                y_node = Node(y)
                hash_node[y] = y_node
            y_node = hash_node[y]
        
            x_node.neighbors[y] = values[i]
            y_node.neighbors[x] = 1 / values[i]
        
        ans = []
        record = {}
        for start, end in queries:
            # 寻找一条从start到end的路径
            if (start, end) in record:
                ans.append(record[(start, end)])
                continue
            if start not in hash_node or end not in hash_node:
                ans.append(-1.0)
                continue
            if start == end:
                ans.append(1.0)
                continue
            q = deque()
            visited = set([start])
            q.append((start, 1))
            flag = False

            while q:
                cnt, res = q.popleft()
                for nxt, val in hash_node[cnt].neighbors.items():
                    if nxt not in visited:
                        visited.add(nxt)
                        nxt_res = res * val
                        if nxt == end:
                            flag = True
                            ans.append(nxt_res)
                            break
                        else:
                            q.append((nxt, nxt_res))
                if flag:
                    break
            if not flag:
                ans.append(-1.0)
            
            record[(start, end)] = ans[-1]
            record[(end, start)] = 1 / ans[-1]
    
        return ans
            




"""
--TESTCASE BEGIN--
TestCase 0: [["a","b"],["b","c"]],[2.0,3.0],[["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
TestCase 1: [["a","b"],["b","c"],["bc","cd"]],[1.5,2.5,5.0],[["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
TestCase 2: [["a","b"]],[0.5],[["a","b"],["b","a"],["a","c"],["x","y"]]
--TESTCASE END--
""" 

print(Solution().calcEquation([["a","b"],["b","c"]],[2.0,3.0],[["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]))
