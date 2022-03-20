from typing import List

class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        n1 = []
        for num in nums:
            if not n1:
                n1.append(num)
            else:
                if num != n1[-1]:
                    n1.append(num)
        
        count = 0
        for i in range(1, len(n1) - 1):
            if n1[i - 1] < n1[i] and n1[i] > n1[i + 1] or n1[i - 1] > n1[i] and n1[i + 1] > n1[i]:
                count += 1
        return count