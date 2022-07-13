from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = 1
        right = 1
        ans = [1 for i in range(len(nums))]

        for i in range(len(nums)):
            ans[i] *= left
            left *= nums[i]

            ans[len(nums) - 1 - i] *= right
            right *= nums[len(nums) - 1 - i]

        return ans

