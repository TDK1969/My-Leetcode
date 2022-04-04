"""
日期: 2022-04-04
题目: 区域和检索 - 数组可修改
链接: https://leetcode-cn.com/problems/range-sum-query-mutable/
"""
from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        preSum = []
        temp = 0
        for num in nums:
            temp += num
            preSum.append(temp)
        self.preSum = preSum

    def update(self, index: int, val: int) -> None:
        for i in range(index, len(self.n)):
            self.preSum[i] += val
    
    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.preSum[right]
        else:
            return self.preSum[right] - self.preSum[left - 1]
        




# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)