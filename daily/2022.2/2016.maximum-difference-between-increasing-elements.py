from typing import List
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        maxDiff = 0
        tempDiff = 0
        for i in range(len(nums) - 1):
            tempDiff += nums[i + 1] - nums[i]
            maxDiff = max(maxDiff, tempDiff)
            if tempDiff < 0:
                tempDiff = 0
            
        return maxDiff if maxDiff != 0 else -1

