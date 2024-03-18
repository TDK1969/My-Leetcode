import requests
from datetime import datetime
import os
import sys
import json

header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv2.0.1) Gecko/20100101 Firefox/4.0.1',
}

book_name = "top-interview-150"

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
    url = "https://leetcode.cn/graphql/"

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
            if i["lang"] == "Python3":
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
    url = "https://leetcode.cn/graphql/"

    res:requests.Response = requests.post(
        url=url,
        headers=header,
        json=payload
    )
    content = '\n\n"""\n--TESTCASE BEGIN--\n'
    if res.status_code == 200:
        print('获取测试用例成功')
        res = res.json()
        testcase_str: str = res["data"]["question"]["jsonExampleTestcases"]
        testcase_str = testcase_str.replace('\\n', ',')
        json_data = json.loads(testcase_str)
        
        for i, testcase in enumerate(json_data):
            content += f"TestCase {i}: " + testcase.replace("null", "None") + "\n"
        
    else:
        print('获取测试用例失败')
    
    content += '--TESTCASE END--\n""" \n'
    return content

def CreateSolutionFile(name:str, title: str, chineseTitle: str, content: str, testCaseContent: str):
    '''创建每日一题的文件

    Args:
        name (str): 文件名
    '''
    solutionPath = f"/home/TDK/Study/My-Leetcode/LeetCode Book/{book_name}/{name}.py"
    if os.path.exists(solutionPath):
        print("文件已存在")
    timeStr = datetime.now().strftime('%Y-%m-%d')
    with open(solutionPath, "w+") as f:
        preContent = f'"""\n日期: {timeStr}\n题目: {chineseTitle}\n链接: https://leetcode-cn.com/problems/{title}/\n"""\n\nfrom typing import *\nfrom collections import *\nfrom leetcode_utils import *\n'
        
        f.write(preContent + content + testCaseContent)
    print("文件创建成功")

def main():

    assert len(sys.argv) == 2, "参数个数错误"
    question_url = sys.argv[1]
    question_name = question_url.split("/")[4]

    question_id, titleCn, content = GetSolutionContent(question_name)
    testCaseContent = GetSolutionTestCase(question_name)
    CreateSolutionFile(f"{question_id}.{question_name}", question_name, titleCn, content, testCaseContent)


main()



