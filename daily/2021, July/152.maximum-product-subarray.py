from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_pre = float("-inf")

        temp_max_pre = 1
        temp_min_pre = 1
        for num in nums:
            if num >= 0:
                temp_max_pre *= num
                temp_min_pre *= num
            else:
                temp_max_pre, temp_min_pre = temp_min_pre * num, temp_max_pre * num
            max_pre = max(max_pre, temp_max_pre)

            if temp_max_pre <= 0:
                temp_max_pre = 1
            if temp_min_pre >= 0:
                temp_min_pre = 1

        return max_pre

test = Solution()
print(test.maxProduct([2,3,-2,4]))

