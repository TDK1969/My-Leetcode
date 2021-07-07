import collections
class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        sum = 0
        presums = set()
        presums.add(0)
        presums_count = collections.defaultdict(int)
        presums_count[0] += 1
        count = 0

        for num in nums:
            sum += num
            if sum - goal in presums:
                count += presums_count[sum - goal]
            presums.add(sum)
            presums_count[sum] += 1

        return count

test = Solution()
print(test.numSubarraysWithSum([0,0,0,0,0], 0))

