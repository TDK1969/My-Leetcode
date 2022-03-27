from typing import List

class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        i = 0
        nxti = 1
        ii = 0

        while i < n:
            if ii & 1 == 0:
                while nxti < n and nums[i] == nums[nxti]:
                    ans += 1
                    nxti += 1
            i, nxti = nxti, nxti + 1
            ii += 1
            
        if ii & 1 == 1:
            ans += 1
        
        return ans

test = Solution()
print(test.minDeletion([0,1,5,4,2,4,7,2,3,0,3,0,0,9,7,5,9,4,3,9,9,2,1,6,3,1,0,7,6,6,6,0,1,7,1,9,4,9,3,3,4,5,0,3,8,7,1,8,4,5]))