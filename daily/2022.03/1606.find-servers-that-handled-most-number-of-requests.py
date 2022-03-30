"""
日期: 2022-03-30
题目: 找到处理最多请求的服务器
链接: https://leetcode-cn.com/problems/find-servers-that-handled-most-number-of-requests/
"""
from typing import List
import heapq
import bisect
from sortedcontainers import SortedList

class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        servers = SortedList(range(k))
        
        endtime = []
        heapq.heapify(endtime)

        taskCnt = [0 for _ in range(k)]
        
        for i, task in enumerate(arrival):
            while endtime:
                end, server = heapq.heappop(endtime)
                if end <= task:
                    # 服务器已完成，加入空闲
                    servers.add(server)
                else:       
                    heapq.heappush(endtime, (end, server))
                    break
            
            if servers:
                # 如果有服务器空闲
                index = servers.bisect_left(i % k)
                if index == len(servers):
                    index = 0
                server = servers[index]
                heapq.heappush(endtime, (task + load[i], server))
                taskCnt[server] += 1
                servers.remove(server)
            
        maxBusy = max(taskCnt)
        ans = []
        for i, task in enumerate(taskCnt):
            if task == maxBusy:
                ans.append(i)
        
        return ans

test = Solution()
print(test.busiestServers(3
,[1,2,3,4,8,9,10]
,[5,2,10,3,1,2,2]))

            
