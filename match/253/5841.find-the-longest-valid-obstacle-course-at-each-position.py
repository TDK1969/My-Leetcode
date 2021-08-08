from typing import List
import bisect

class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        n = len(obstacles)
        ans = [1] * n
        l = []  # 维护递增序列
        for i, a in enumerate(obstacles):
            p = bisect.bisect_right(l, a)  # 寻找当前的高度在递增序列中插入的位置
            if p == len(l):
                l.append(a)  #
            else:
                l[p] = a  # 贪心策略，使构成的递增序列最小
            ans[i] = p + 1
        return ans

test = Solution()
print(test.longestObstacleCourseAtEachPosition([5,1,5,5,1,3,4,5,1,4]))