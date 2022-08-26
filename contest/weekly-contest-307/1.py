from typing import *
from collections import *

class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        energy_time = max(sum(energy) - initialEnergy + 1, 0)
 
        get_exp = [0]
        for i in experience:
            get_exp.append(get_exp[-1] + i)
        need_exp = [max(experience[i] - get_exp[i], 0) for i in range(len(experience))]
        experience_time = max(max(need_exp) - initialExperience + 1, 0)
        return energy_time + experience_time

test = Solution()
print(test.minNumberOfHours(initialEnergy = 2, initialExperience = 4, energy = [1], experience = [3]))