from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        """
        要求时间复杂度O(logn)，因此需要使用二分
        二分的依据是有序数组中只存在一个单一元素，因此会导致数组长度为奇数
        因此进行二分时可以找到中心位置，两侧的元素数量相等，两侧元素数量的奇偶也是关键
        此时，判断中心位置的元素与左还是右的元素相等
        - 如果都不相等，则中心元素为单一元素
        - 如果与左边相等
        - 如果与右边相等
        """
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            half = (right - left) // 2
            if left == right:
                return nums[left]
            elif nums[mid] == nums[mid - 1]:
                if half & 1:
                    left = mid + 1
                else:
                    right = mid - 2
            elif nums[mid] == nums[mid + 1]:
                if half & 1:
                    right = mid - 1
                else:
                    left = mid + 2
            else:
                return nums[mid]
        return -1

test = Solution()
print(test.singleNonDuplicate([3,3,7,7,10,11,11]))
