from typing import List
import bisect

class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        def check(t: int) -> bool:
            ans = 0
            for bus in time:
                ans += t // bus
            return ans >= totalTrips

        left = 0
        right = totalTrips * min(time)
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                ans = mid
                right = mid - 1
            else:

                left = mid + 1
        return ans

test = Solution()
print(test.minimumTime(time = [1,2,3], totalTrips = 5))





