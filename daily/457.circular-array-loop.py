from typing import List


class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(n):
            if nums[i] < 0:
                nums[i] %= n
                nums[i] -= n
            else:
                nums[i] %= n

        for i in range(n):
            loop = set()
            loop.add(i)
            nxt = (i + nums[i]) % n
            while nxt not in loop and nums[nxt] * nums[i] > 0:
                loop.add(nxt)
                nxt = (nxt + nums[nxt]) % n
            if nxt == i and len(loop) > 1:
                return True

        return False

test = Solution()
print(test.circularArrayLoop([-2,1,-1,-2,-2]))