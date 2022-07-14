import requests
from bs4 import BeautifulSoup
from typing import *
from datetime import datetime
import os
import sys

book_url = "https://leetcode.cn/problem-list/2ckc81c/?page={}"
page_index = 1
problem_index = 1

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
}

def get_soup(url):
    r = requests.get(url, headers=headers)
    print(r.text)

    return BeautifulSoup(r.text, 'lxml')

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
        headers=headers,
        json=payload
    )

    content = ""
    if res.status_code == 200:
        #print('获取每日一题模板成功')
        
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

def CreateSolutionFile(name:str, title: str, chineseTitle: str, content: str):
    '''创建每日一题的文件

    Args:
        name (str): 文件名
    '''
    leetcodeBasePath = "/home/tdk/Study/My-Leetcode/LeetCode 精选 TOP 面试题/"
    if not os.path.exists(leetcodeBasePath):
        os.mkdir(leetcodeBasePath)
    solutionPath = f"{leetcodeBasePath}{name}.py"
    if os.path.exists(solutionPath):
        print("文件已存在")
    timeStr = datetime.now().strftime('%Y-%m-%d')
    with open(solutionPath, "w+") as f:
        preContent = f'"""\n日期: {timeStr}\n题目: {chineseTitle}\n链接: https://leetcode-cn.com/problems/{title}/\n"""\n\nfrom typing import *\nfrom collections import *\n'
        
        f.write(preContent + content)
    #print("文件创建成功")


def get_page(index: int) -> List[str]:
    soup = get_soup("https://leetcode.cn/problem-list/2ckc81c/?page=2")

    row_group = soup.find(role="rowgroup")
    row = row_group.find_all(role="row")
    for i in row:
        problem = i.find(class_="h-5 hover:text-primary-s dark:hover:text-dark-primary-s")
        t = problem.get("href")
        
        question_name = t.split("/")[-1]
        print(question_name)

        question_id, titleCn, content = GetSolutionContent(question_name)
        CreateSolutionFile(f"{question_id}.{question_name}", question_name, titleCn, content)

get_page(2)