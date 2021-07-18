from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sub_sum = 0
        temp_sum = 0
        for num in nums:
            temp_sum += num
            sub_sum = max(sub_sum, temp_sum)
            if temp_sum < 0:
                temp_sum = 0
        if not sub_sum:
            return max(nums)
        return sub_sum

test = Solution()
print(test.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))