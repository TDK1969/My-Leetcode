"""
日期: 2023-10-31
题目: 每棵子树内缺失的最小基因值
链接: https://leetcode-cn.com/problems/smallest-missing-genetic-value-in-each-subtree/
"""

from typing import *
from collections import *
class Solution:
    def smallestMissingValueSubtree(self, parents: List[int], nums: List[int]) -> List[int]:
        #  只有含有基因值为1的节点的链路需要修改,其他节点的缺失最小基因值都为1
        n = len(parents)
        ans = [1] * n

        if 1 not in nums:
            return ans
        
        children = defaultdict(list)
        for node, parent in enumerate(parents):
            children[parent].append(node)
        
        path = [nums.index(1)]
        while parents[path[-1]] != -1:
            path.append(parents[path[-1]])
        
        gen = [0] * ((10 ** 5) + 5)
        ptr = 1
        def dfs(root: int):
            gen[nums[root]] = 1
            for child in children[root]:
                if gen[nums[child]] == 0:
                    dfs(child)
                    
        for node in path:
            dfs(node)
            while gen[ptr] != 0:
                ptr += 1
            ans[node] = ptr
        
        return ans

print(Solution().smallestMissingValueSubtree(parents = [-1,0,1,0,3,3], nums = [5,4,6,2,1,3]))

            



        