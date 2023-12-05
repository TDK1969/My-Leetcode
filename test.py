'''
Author: TDK
Date: 2022-09-09 16:32:08
LastEditors: TDK 793065367@qq.com
LastEditTime: 2023-11-15 22:33:29
FilePath: /My-Leetcode/test.py
Description: 
'''
import json

# 提供的字符串
input_str = '[\"[3,5,1,6,2,0,8,null,null,7,4]\\n5\\n1\", \"[3,5,1,6,2,0,8,null,null,7,4]\\n5\\n4\", \"[1,2]\\n1\\n2\"]'

# 移除转义字符
input_str = input_str.replace('\\n', ',')

# 将字符串解析为 JSON 格式
json_data = json.loads(input_str)

# 将 JSON 数据转换为格式化字符串
formatted_str = json.dumps(json_data, indent=2)

# 打印格式化的 JSON 字符串
print(formatted_str)
