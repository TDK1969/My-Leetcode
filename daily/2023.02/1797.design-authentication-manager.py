"""
日期: 2023-02-09
题目: 设计一个验证系统
链接: https://leetcode-cn.com/problems/design-authentication-manager/
"""

from typing import *
from collections import *
import heapq
class AuthenticationManager:
    class ListNode:
        def __init__(self, val: int, tokenId: str, pre=None, nxt=None) -> None:
            self.val = val
            self.tokenId = tokenId
            self.pre = pre
            self.nxt = nxt

    def __init__(self, timeToLive: int):
        self.auth = dict()
        self.head = self.ListNode(-1, "")
        self.tail = self.ListNode(-1, "")
        self.head.nxt = self.tail
        self.tail.pre = self.head
        self.ttl = timeToLive


    def generate(self, tokenId: str, currentTime: int) -> None:
        new_node = self.ListNode(currentTime + self.ttl, tokenId, None, None)
        new_node.pre = self.tail.pre
        self.tail.pre.nxt = new_node
        new_node.nxt = self.tail
        self.tail.pre = new_node

        self.auth[tokenId] = new_node
        
    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId not in self.auth:
            return
        elif self.auth[tokenId].val <= currentTime:
            # 验证码过期
            return
        else:
            node = self.auth[tokenId]
            node.val = currentTime + self.ttl

            node.pre.nxt = node.nxt
            node.nxt.pre = node.pre

            node.pre = self.tail.pre
            self.tail.pre.nxt = node
            node.nxt = self.tail
            self.tail.pre = node

    def countUnexpiredTokens(self, currentTime: int) -> int:
        p = self.head.nxt
        while p != self.tail and p.val <= currentTime:
            self.auth.pop(p.tokenId)
            p = p.nxt
        self.head.nxt = p
        p.pre = self.head
        
        return len(self.auth)
            
        

t = AuthenticationManager(5)
t.renew("aaa", 1)
t.generate("aaa", 2)
print(t.countUnexpiredTokens(5))
t.generate("bbb", 7)
t.renew("aaa", 8)
t.renew("bbb", 10)
print(t.countUnexpiredTokens(15))
# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)