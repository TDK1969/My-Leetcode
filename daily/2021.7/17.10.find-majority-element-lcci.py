class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: list[int]
        :rtype: int
        """
        count = 0
        major = -1

        for num in nums:
            if count == 0:
                major = num
            if major == num:
                count += 1
            else:
                count -= 1

        if nums.count(major) * 2 > len(nums):
            return major
        else:
            return -1