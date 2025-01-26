from typing import List

class ListNode:
    def __init__(self, number: int, pre: "ListNode"=None, nxt: "ListNode"=None):
        self.number = number
        self.pre = pre
        self.nxt = nxt

def solution(n: int, q: int, op: List[List[int]]) -> List[int]:
    stone = dict()
    for i in range(1, n + 1):
        stone[i] = ListNode(i)
    
    start = ListNode(-1)
    end = ListNode(-1)

    for i in range(1, n + 1):
        if i > 1:
            stone[i].pre = stone[i - 1]
        if i < n:
            stone[i].nxt = stone[i + 1]
    
    start.nxt = stone[1]
    stone[1].pre = start

    stone[n].nxt = end
    end.pre = stone[n]
    
    for a, b, p in op:
        if p == 0:
            # a 放在 b 前
            stone[a].pre.nxt = stone[a].nxt
            stone[a].nxt.pre = stone[a].pre
            
            stone[b].pre.nxt = stone[a]
            stone[a].pre = stone[b].pre
            stone[b].pre = stone[a]
            stone[a].nxt = stone[b]
        else:
            # a 放在 b 后
            stone[a].pre.nxt = stone[a].nxt
            stone[a].nxt.pre = stone[a].pre

            stone[b].nxt.pre = stone[a]
            stone[a].nxt = stone[b].nxt
            stone[b].nxt = stone[a]
            stone[a].pre = stone[b]
    
    ptr = start.nxt
    ans = []
    while ptr.number != -1:
        ans.append(str(ptr.number))
        ptr = ptr.nxt
    
    return ans

print(solution(5, 3, [[1,2,1], [3,2,0], [5,4,0]]))


