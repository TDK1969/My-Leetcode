from typing import List


class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        ans = [0 for _ in range(n)]
        for first, last, seats in bookings:
            ans[first - 1] += seats
            if last < n:
                ans[last] -= seats
        temp = []
        pre = 0
        for delta in ans:
            pre += delta
            temp.append(pre)
        return temp

test = Solution()
print(test.corpFlightBookings([[1,2,10],[2,3,20],[2,5,25]], 5))