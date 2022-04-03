from typing import List


class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        left = 0
        right = sum(candies) // k
        candies.sort(reverse=True)

        if right == 0:
            return 0
        right += 1
        def check(c: int) -> bool:
            count = 0
            for candy in candies:
                count += candy // c

                if count >= k:
                    return True
            return False
        
        while left < right:
            mid = (left + right) // 2
            if (check(mid)):
                left = mid + 1
            else:
                right = mid
        
        return left - 1

test = Solution()
print(test.maximumCandies([2,5], 11))