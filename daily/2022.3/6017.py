from typing import List

class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        nums.sort()
        tempK = k
        tempSum = 0
        for num in nums:
            if num <= tempK:
                tempK += 1
                tempSum += num
        return (1 + tempK) * tempK // 2 - tempSum
        


test = Solution()
print(test.minimalKSum(nums = [96,44,99,25,61,84,88,18,19,33,60,86,52,19,32,47,35,50,94,17,29,98,22,21,72,100,40,84],k = 35))