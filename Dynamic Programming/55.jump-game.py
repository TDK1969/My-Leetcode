from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        energy = 1
        n = len(nums)
        step = -1

        while energy:
            energy -= 1
            step += 1
            if step == n - 1:
                return True
            energy = max(energy, nums[step])
        return False
test = Solution()
print(test.canJump([3,2,1,0,4]))

