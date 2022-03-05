from typing import List


class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        ans = 0
        stack = []

        for i in nums:
            if not stack:
                stack.append(i)
            

        return ans

test = Solution()
print(test.subArrayRanges(nums = [4,-2,-3,4,1]))
