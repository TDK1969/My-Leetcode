"""
日期: 2022-04-09
题目: 到达终点
链接: https://leetcode-cn.com/problems/reaching-points/
"""
class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while tx and ty:
            if tx == sx and ty == sy:
                return True
            if tx == ty:
                return False
            if tx > ty:
                tx -= max((tx - sx) // ty, 1) * ty
            elif ty > tx:
                ty -= max((ty - sy) // tx, 1) * tx
        
        return False

test = Solution()
print(test.reachingPoints(sx = 9, sy = 10, tx = 9, ty = 19))