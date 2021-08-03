from typing import List


class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        abs_diff = []
        diff_sum = 0
        for i in range(len(nums1)):
            diff_sum += abs(nums1[i] - nums2[i])
            abs_diff.append(abs(nums1[i] - nums2[i]))

        if diff_sum == 0:
            return 0

        min_sum = diff_sum
        sorted_nums1 = sorted(nums1)
        for i in range(len(nums2)):
            l = 0
            r = len(nums1) - 1
            while l < r - 1:
                mid = (l + r) // 2
                if sorted_nums1[mid] == nums2[i]:
                    r = mid
                    break
                elif sorted_nums1[mid] < nums2[i]:
                    l = mid
                else:
                    r = mid
            new_diff = min(abs(nums2[i] - sorted_nums1[l]), abs(nums2[i] - sorted_nums1[r]))
            min_sum = min(min_sum, diff_sum - abs_diff[i] + new_diff)

        return min_sum % (10**9 + 7)


test = Solution()
print(test.minAbsoluteSumDiff([1,28,21], [9,21,20]))



