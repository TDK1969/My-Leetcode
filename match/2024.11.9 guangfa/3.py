from collections import deque
class Solution:
    def countRoutesNum(self , graphStr: str, startStr: str, endStr: str) -> int:
        # write code here
        graph = graphStr[1:-1]
        sep = graph.split(":")
        main_node = sep[0]
        edges = dict()
        for i in range(1, len(sep)):
            s2 = sep[i].split(")")
            nxt_nodes = s2[0][1:].split(",")
            edges[main_node] = nxt_nodes
            for node in nxt_nodes:
                if node not in edges:
                    edges[node] = []
            main_node = s2[1][1:]
        
        visited = set()
        q = deque()
        q.append(startStr)
        visited.add(startStr)
        ans = 0

        while q:
            cur = q.popleft()
            if cur == endStr:
                ans += 1
            else:
                for nxt in edges[cur]:
                    if nxt == endStr:
                        ans += 1
                    elif nxt not in visited:
                        visited.add(nxt)
                        q.append(nxt)
            

        return ans

print(Solution().countRoutesNum("(A:(B,C),B:(D),C:(D))", "A", "D"))

