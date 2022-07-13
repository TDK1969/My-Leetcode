"""
日期: 2022-07-13
题目: 行星碰撞
链接: https://leetcode-cn.com/problems/asteroid-collision/
"""

from typing import *
from collections import *
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for star in asteroids:
            flag = True

            while flag and stack and stack[-1] > 0 and star < 0:
                flag = (stack[-1] + star) < 0
                if flag:
                    stack.pop()
            
            if flag:
                stack.append(star)
        
        return stack



        """
        stack = []
        ans = []
        for star in asteroids:
            if not stack:
                if star < 0:
                    ans.append(star)
                else:
                    stack.append(star)
            else:
                if star > 0:
                    stack.append(star)
                else:
                    while stack:
                        t = stack[-1]
                        if t + star < 0:
                            stack.pop()
                        elif t + star == 0:
                            stack.pop()
                            break
                        else:
                            break
                    if not stack and t + star < 0:
                        ans.append(star)
        ans += stack
        return ans
        """

test = Solution()
print(test.asteroidCollision(asteroids =  [10,2,-5]))
