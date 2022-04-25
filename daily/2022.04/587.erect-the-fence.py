"""
日期: 2022-04-23
题目: 安装栅栏
链接: https://leetcode-cn.com/problems/erect-the-fence/
"""
from typing import List


class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        min_y = 105
        p = []
        for tree in trees:
            if tree[1] < min_y:
                min_y = tree[1]
                p = tree

        trees.remove(p)
        trees.sort(key=lambda x:(x[0] - p[0]) / ((x[0] - p[0]) ** 2 + (x[1] - p[1]) ** 2) ** 0.5, reverse=True)
        
        ans = [p]
        ans.append(trees[0])
        
        def check(p: List[int], q: List[int], r: List[int]):
            return (r[1] - p[1]) * (q[0] - p[0]) - (r[0] - p[0])(q[1] - p[1])

        for tree in trees[1:]:
            if check(ans[-2], tree, ans[-1]) >= 0:
                ans.append(tree)
            
                


    
test = Solution()
print(test.outerTrees([[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]))


