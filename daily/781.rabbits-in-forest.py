class Solution(object):
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        number = [0] * 1005
        count = 0
        if not answers:
            return 0

        for i in answers:
            if number[i + 1] % (i + 1) == 0:
                count += i + 1
            number[i + 1] += 1

        return count
