from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (l + r) >> 1
            if nums[mid] >= target:
                r = mid
            else:
                l = mid + 1
        if nums[r] != target:
            return 0
        a = r

        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (l + r + 1) >> 1
            if nums[mid] <= target:
                l = mid
            else:
                r = mid - 1

        if nums[r] != target:
            return 0
        b = r

        return b - a + 1

test = Solution()
print(test.search([1], 0))



        