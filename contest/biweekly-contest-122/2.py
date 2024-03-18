from typing import *
class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        l = []
        n = len(nums)
        i = 0
        while i < n:
            i_cnt = bin(nums[i]).count("1")
            j = i + 1
            while j < n and bin(nums[j]).count("1") == i_cnt:
                j += 1
            l.append(min(nums[i:j]))
            l.append(max(nums[i:j]))
            i = j
        
        return l == sorted(l)
    
print(Solution().canSortArray([8,4,2,30,15]))
        
