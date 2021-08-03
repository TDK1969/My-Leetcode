from typing import List
from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        maxtime = 0
        visited = set()
        network = defaultdict(lambda: defaultdict(int))

        for s, e, w in times:
            network[s][e] = w

        queue = []
        heapq.heapify(queue)

        heapq.heappush(queue, (0, k))

        while queue:
            time, net = heapq.heappop(queue)
            if net not in visited:
                maxtime = max(maxtime, time)
                visited.add(net)
                for e, w in network[net].items():
                    if e not in visited:
                        heapq.heappush(queue, (time + w, e))

        if len(visited) != n:
            return -1
        return maxtime

test = Solution()
print(test.networkDelayTime([[1,2,1],[2,3,2],[1,3,4]], 3, 1))



