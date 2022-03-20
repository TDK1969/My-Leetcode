from typing import List
import heapq

class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        queue = []
        pair = {}
        n = len(times)
        for i in range(n):
            arrive = times[i][0]
            leave = times[i][1]
            queue.append((-arrive, 1, i))
            queue.append((-leave, 2, i))
        queue.sort()

        seats = [i for i in range(10**4 + 1)]
        heapq.heapify(seats)

        while queue:
            time, t, num = queue.pop()
            if t == 1:
                seat = heapq.heappop(seats)
                if num == targetFriend:
                    return seat
                pair[num] = seat
            else:
                seat = pair[num]
                heapq.heappush(seats, seat)
        return -1


test = Solution()
print(test.smallestChair( [[3,10],[1,5],[2,6]], 0))
