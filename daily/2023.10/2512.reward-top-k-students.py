"""
日期: 2023-10-11
题目: 奖励最顶尖的 K 名学生
链接: https://leetcode-cn.com/problems/reward-top-k-students/
"""

from typing import *
from collections import *
import heapq
class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        h = []
        heapq.heapify(h)
        words_dict = dict()
        for p_word in positive_feedback:
            words_dict[p_word] = 3
        for n_word in negative_feedback:
            words_dict[n_word] = -1
    
        for i in range(len(report)):
            score = sum([words_dict.get(word, 0) for word in report[i].split(" ")])
            heapq.heappush(h, (-score, student_id[i]))
        
        res = heapq.nsmallest(k, h)
        return [i[1] for i in res]

test = Solution()
print(test.topStudents(
    positive_feedback = ["fkeofjpc","qq","iio"], 
    negative_feedback = ["jdh","khj","eget","rjstbhe","yzyoatfyx","wlinrrgcm"], 
    report = ["rjstbhe eget kctxcoub urrmkhlmi yniqafy fkeofjpc iio yzyoatfyx khj iio","gpnhgabl qq qq fkeofjpc dflidshdb qq iio khj qq yzyoatfyx","tizpzhlbyb eget z rjstbhe iio jdh jdh iptxh qq rjstbhe","jtlghe wlinrrgcm jnkdbd k iio et rjstbhe iio qq jdh","yp fkeofjpc lkhypcebox rjstbhe ewwykishv egzhne jdh y qq qq","fu ql iio fkeofjpc jdh luspuy yzyoatfyx li qq v","wlinrrgcm iio qq omnc sgkt tzgev iio iio qq qq","d vhg qlj khj wlinrrgcm qq f jp zsmhkjokmb rjstbhe"], 
    student_id = [96537918,589204657,765963609,613766496,43871615,189209587,239084671,908938263], 
    k = 3
    )
)