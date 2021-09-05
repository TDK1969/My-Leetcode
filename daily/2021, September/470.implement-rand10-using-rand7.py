# The rand7() API is already defined for you.
def rand7():
    return 1
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        while True:
            res = (rand7() - 1) * 7 + rand7()
            if res <= 40:  # 拒绝采样
                break
        return res % 10 + 1  # 这个+1把0~9变为1~10

