from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False

        tempMin = float("inf")
        globalMin = float("inf")
        tempSec = float("inf")
        globalSec = float("inf")

        for num in nums:
            if num < tempMin:
                tempMin = num
                if tempSec != float("inf"):
                    globalSec = tempSec
                tempSec = float("inf")
                if num < globalMin:
                    globalMin = num
            elif num > tempSec:
                return True
            elif num > globalSec:
                return True
            elif tempMin < num < tempSec:
                tempSec = num

        return False

test = Solution()
print(test.increasingTriplet([20,100,10,12,5,13]))



