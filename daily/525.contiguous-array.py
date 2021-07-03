class Solution:
    def findMaxLength(self, nums) -> int:
        numsum = 0
        presums = set()
        presums.add(0)
        record = {0: -1}
        length = 0
        for i in range(len(nums)):
            num = nums[i]
            if num:
                numsum += 1
            else:
                numsum -= 1
            if numsum in presums:
                preindex = record[numsum]
                length = max(length, i - preindex)
            else:
                presums.add(numsum)
                record[numsum] = i

        return length

test = Solution()
print(test.findMaxLength([0, 1, 0, 0, 1, 0]))