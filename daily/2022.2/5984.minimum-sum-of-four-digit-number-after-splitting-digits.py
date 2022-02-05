class Solution:
    def minimumSum(self, num: int) -> int:
        nums = []
        for i in range(4):
            nums.append(num % 10)
            num = num // 10
        nums.sort()

        return nums[0] * 10 + nums[1] * 10 + nums[2] + nums[3]