from typing import List
from collections import Counter

class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        ans = 0
        # 记录每个节点的度,最终合法的方案中每个节点的度都应该为0
        degrees = [0 for _ in range(n)]
        def dfs(index: int, requestsNum: int):
            '''使用DFS+回溯进行解决

            Args:
                index (int): 当前处理的request的下标
                requestsNum (int): 已经选择的request数量        
            '''
            
            if index == len(requests):
                for degree in degrees:
                    # 如果存在某个节点的度不为0,则不合法,直接退出
                    if degree:
                        return
                # 如果是合法方案,则与记录的最大值对比
                nonlocal ans
                ans = max(ans, requestsNum)
                return
            
            # 不选择当前request,不进行任何处理,直接下一个
            dfs(index + 1, requestsNum)

            # 选择当前request,对度进行处理
            degrees[requests[index][0]] -= 1
            degrees[requests[index][1]] += 1
            dfs(index + 1, requestsNum + 1)
            # 恢复度,进行回溯
            degrees[requests[index][0]] += 1
            degrees[requests[index][1]] -= 1
        
        dfs(0, 0)
        return ans

test = Solution()
print(test.maximumRequests(n = 5, requests = [[0,1],[1,0],[0,1],[1,2],[2,0],[3,4]]))





