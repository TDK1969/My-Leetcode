'''
Author: TDK 793065367@qq.com
Date: 2023-11-15 20:42:33
LastEditors: TDK
LastEditTime: 2023-11-16 19:34:01
FilePath: /My-Leetcode/go_mks.py
Description: 
'''
import requests
from datetime import datetime
import os
import sys
import json

header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv2.0.1) Gecko/20100101 Firefox/4.0.1',
}

def GetSolutionContent(title: str) -> str:
    '''获取每日一题的模板

    Args:
        title (str): title

    Returns:
        str: python3的模板代码
    '''
    payload = {
        "operationName": "questionData",
        "variables": {
            "titleSlug": title
        },
        "query": "query questionData($titleSlug: String!) {\n  question(titleSlug: $titleSlug) {\n questionFrontendId\n  translatedTitle \n  codeSnippets {\n      lang\n      langSlug\n      code\n      __typename\n    }\n}\n}\n"
    }
    url = "https://leetcode-cn.com/graphql/"

    res:requests.Response = requests.post(
        url=url,
        headers=header,
        json=payload
    )

    content = ""
    if res.status_code == 200:
        print('获取每日一题模板成功')
        
        res = res.json()
        codeSnippet = res["data"]["question"]["codeSnippets"]
        for i in codeSnippet:
            if i["lang"] == "Go":
                content = i["code"]
                break
    else:
        print('获取每日一题模板失败')
    
    ans = (res["data"]["question"]["questionFrontendId"], res["data"]["question"]["translatedTitle"], content)
    return ans

def GetSolutionTestCase(title: str) -> str:
    payload = {
        "query": "\n    query consolePanelConfig($titleSlug: String!) {\n  question(titleSlug: $titleSlug) {\n    questionId\n    questionFrontendId\n    questionTitle\n    enableRunCode\n    enableSubmit\n    enableTestMode\n    jsonExampleTestcases\n    exampleTestcases\n    metaData\n    sampleTestCase\n  }\n}\n    ",
        "variables": {
            "titleSlug": title
        },
        "operationName": "consolePanelConfig"
    }
    url = "https://leetcode-cn.com/graphql/"

    res:requests.Response = requests.post(
        url=url,
        headers=header,
        json=payload
    )
    content = "\n\n/*--TESTCASE BEGIN--\n"
    if res.status_code == 200:
        print('获取测试用例成功')
        res = res.json()
        testcase_str: str = res["data"]["question"]["jsonExampleTestcases"]
        testcase_str = testcase_str.replace('\\n', ',')
        json_data = json.loads(testcase_str)
        
        for i, testcase in enumerate(json_data):
            content += f" *TestCase {i}: " + testcase.replace("null", "nil").replace("[", "{").replace("]", "}") + "\n"
        
    else:
        print('获取测试用例失败')
    
    content += " *--TESTCASE END--\n */ \n"
    return content    

def CreateSolutionFile(name:str, title: str, chineseTitle: str, content: str, testCaseContent: str):
    '''创建每日一题的文件

    Args:
        name (str): 文件名
    '''
    monthDir = datetime.now().strftime("%Y.%m")
    leetcodeBasePath = "/home/tdk/Study/My-Leetcode/daily/"
    if not os.path.exists(leetcodeBasePath + monthDir):
        os.makedirs(leetcodeBasePath + monthDir)

    #solution_path = f"{leetcodeBasePath}{monthDir}/{name}.py"
    solution_dir = f"/home/tdk/Study/My-Leetcode/LeetCodeGo/{name}"
    if not os.path.exists(solution_dir):
        os.makedirs(solution_dir, exist_ok=True)
    solution_path = f"/home/tdk/Study/My-Leetcode/LeetCodeGo/{name}/{name}.go"
    if os.path.exists(solution_path):
        print("文件已存在")
    timeStr = datetime.now().strftime('%Y-%m-%d')
    with open(solution_path, "w+") as f:
        preContent = f'/* INTRODUCTION\n *日期: {timeStr}\n *题目: {chineseTitle}\n *链接: https://leetcode-cn.com/problems/{title}/\n */\n\npackage main\nimport (\n\t"fmt"\n)\n//--CODE BEGIN--\n\n//lint:ignore U1000 Ignore unused function check\n'
        after_content = f'\n//--CODE END--\n'
        test_content = "func main() {\n\n}"
        f.write(preContent + content + after_content + testCaseContent + test_content)
    print("文件创建成功")



def main():

    assert len(sys.argv) == 2, "参数个数错误"
    question_url = sys.argv[1]
    question_name = question_url.split("/")[4]

    question_id, titleCn, content = GetSolutionContent(question_name)
    testCaseContent = GetSolutionTestCase(question_name)
    CreateSolutionFile(f"{question_id}.{question_name}", question_name, titleCn, content, testCaseContent)


main()



