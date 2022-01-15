from typing import List


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        cnt = 1
        i1, i2 = 0, 0
        n1, n2 = len(nums1), len(nums2)
        ans = [[nums1[0], nums2[0]]]

        while cnt < k:
            next1 = i1 + 1 if i1 < n1 - 1 else n1 - 1
            next2 = i2 + 1 if i2 < n2 - 1 else n2 - 1

            if nums1[i1] + nums2[next2] > nums1[next1] + nums2[i2]:
                ans.append([nums1[next1], nums2[i2]])
                cnt += 1
                i1 = next1
            else:
                ans.append([nums1[i1], nums2[next2]])
                cnt += 1
                i2 = next2

            if cnt == n1 * n2:
                break
            
        return ans

test = Solution()
print(test.kSmallestPairs(nums1 = [1,2], nums2 = [3], k = 3 ))



