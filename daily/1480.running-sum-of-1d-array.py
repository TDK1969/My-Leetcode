from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        presum = 0
        for i, num in enumerate(nums):
            presum += num
            nums[i] = presum
        return nums
