"""
日期: 2024-01-18
题目: 最小基因变化
链接: https://leetcode-cn.com/problems/minimum-genetic-mutation/
"""

from typing import *
from collections import *
from leetcode_utils import *
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        def gene2num(gene: str) -> int:
            t = 0
            for s in gene:
                t = (t << 2) + genes[s]
            return t
        
        visited = set()
        genes = {"A": 0, "C": 1, "G": 2, "T": 3}
        q = deque()
        bank_num = set()
        for gene in bank:
            bank_num.add(gene2num(gene))

        start = gene2num(startGene)
        end = gene2num(endGene)
        q.append((start, 0))
        visited.add(start)

        while q:
            cnt, move = q.popleft()
            if cnt == end:
                return move
            for i in range(8):
                for j in range(4):
                    right = cnt % (4 ** i)
                    left = cnt >> (2 * (i + 1))
                    mid = (cnt >> (2 * i)) % 4
                    nxt = (((left << 2) | j) << (2 * i)) | right
                    if nxt in bank_num and nxt not in visited:
                        visited.add(nxt)
                        q.append((nxt, move + 1))
                    
        
        return -1

print(Solution().minMutation("AACCTTGG", "AATTCCGG", ["AATTCCGG","AACCTGGG","AACCCCGG","AACCTACC"]))
                    
"""
--TESTCASE BEGIN--
TestCase 0: "AACCGGTT","AACCGGTA",["AACCGGTA"]
TestCase 1: "AACCGGTT","AAACGGTA",["AACCGGTA","AACCGCTA","AAACGGTA"]
--TESTCASE END--
""" 
