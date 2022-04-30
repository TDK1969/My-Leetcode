"""
题目: 最小平均差
链接: https://leetcode-cn.com/problems/minimum-average-difference/
"""
from typing import List
class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        presums = []
        temp = 0
        for num in nums:
            temp += num
            presums.append(temp)
        
        ans = 0
        min_diff = float("inf")
        n = len(nums)

        for i in range(n):
            pre = presums[i]
            back = presums[-1] - pre
            if i == n - 1:
                diff = pre // (i + 1)
            else:
                diff = abs((pre // (i + 1)) - (back // (n - i - 1)))
            if diff < min_diff:
                min_diff = diff
                ans = i
        
        return ans

test = Solution()
print(test.minimumAverageDifference([2,5,3,9,5,3]))