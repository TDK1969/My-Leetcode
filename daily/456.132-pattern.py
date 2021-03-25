class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if nums == sorted(nums) or nums == sorted(nums, reverse=True):
            return False

        one = None
        three = None
        for i in range(len(nums)):
            num = nums[i]
            if one is None:
                one = num
            elif three is None:
                if num < one:
                    one = num
                elif num > one + 1:
                    three = num

            if one is not None and three is not None:
                for test_num in range(one + 1, three):
                    if test_num in nums[i + 1:]:
                        return True

                three = None

        return False

test = Solution()
print(test.find132pattern([-2,1,1,-2,1,2]))
