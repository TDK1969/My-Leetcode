from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.schedulers.background import BlockingScheduler
scheduler = BlockingScheduler()
scheduler.configure(timezone="Asia/Shanghai")

import json
from typing import List
import requests
import time
import sys
import os
from datetime import datetime

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv2.0.1) Gecko/20100101 Firefox/4.0.1',
}



def GetCodeDefinition(questionId: int) -> str:
    '''获取代码模板

    Args:
        questionId (int): questionId

    Returns:
        str: 代码模板
    '''
    codeDefinitionAPI = "https://leetcode-cn.com/problems/{}/code-definitions/python3/"
    res = requests.get(
        url=codeDefinitionAPI.format(questionId),
        headers=headers
    )
    return res.json()["code"]


def CreateContestCode(contestTitle:str) -> bool:
    '''获取竞赛的代码模板并创建本地文件

    Args:
        contestTitle (str): 竞赛名

    Returns:
        bool: 是否成功
    '''
    leetcodeBasePath = "/home/TDK/Projects/My-Leetcode/contest/"
    contestInfoAPI = "https://leetcode.cn/contest/api/info/{}/"
    
    if not os.path.exists(leetcodeBasePath + contestTitle): 
        os.makedirs(leetcodeBasePath + contestTitle)
    
    res = requests.get(
        url=contestInfoAPI.format(contestTitle),
        headers=headers,
    )
    res = res.json()
    questions = res["questions"]

    questions.sort(key=lambda x:x["credit"])

    i = 1
    for question in questions:
        titleSlug = question["title_slug"]
        questionId = question["question_id"]
        chineseTitle = question["title"]
        
        preContent = f'"""\n题目: {chineseTitle}\n链接: https://leetcode.cn/problems/{titleSlug}/\n"""\n\nfrom typing import *\nfrom collections import *\nfrom leetcode_utils import *\n'
        #codeDefinition = GetCodeDefinition(questionId)

        #if "List" in codeDefinition:
            #preContent += "\nfrom typing import List\n\n\n"
        
        #preContent += codeDefinition

        with open(f"{leetcodeBasePath + contestTitle}/{i}.{titleSlug}.py", "w+") as f:
            f.write(preContent)
        
        i += 1    

def GetRecentContests() -> List[List[str]]:
    """
    @description  :
    获取48小时内的力扣竞赛信息
    ---------
    @param  :
    无
    -------
    @Returns  :
    返回一个列表，列表中的每个元素也是一个列表
    [竞赛名，封面链接，开始时间]
    -------
    """
    
    s = requests.Session()
    requestPayload = {
        'query':'{\n  contestUpcomingContests {\n    containsPremium\n    title\n    cardImg\n    titleSlug\n    description\n    startTime\n    duration\n    originStartTime\n    isVirtual\n    isLightCardFontColor\n    company {\n      watermark\n      __typename\n    }\n    __typename\n  }\n}\n',
        'variables':{},
        'operationName':None
    }
    response = s.post(url='https://leetcode.cn/graphql/', headers=headers, json=requestPayload)
    assert response.status_code == 200, f'获取力扣竞赛页面时出现错误, status code = {response.status_code}'
    recentContests = response.json()
    recentContests = recentContests['data']['contestUpcomingContests']
    reportContests = []
    
    #reportContests = []
    s.close()

    for contest in recentContests:
        
        title = contest['title']
        imgURL = contest['cardImg']
        startTime = contest['startTime']
        
        if startTime - int(time.time()) < 172800:
            
            timeArray = time.localtime(startTime)
            timeFormat = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
            reportContests.append([title, imgURL, timeFormat])

            
            #定时创建代码文件
            scheduler.add_job(CreateContestCode, "date", run_date=datetime.fromtimestamp(startTime), args=[contest['titleSlug']])


    
    return reportContests

def CheckContests():
    """
    @description  :
    定期任务，向用户通知48小时内的比赛信息
    ---------
    @param  :
    无
    -------
    @Returns  :
    无
    -------
    """
       
    try:
        recentContests = GetRecentContests()
    except Exception as e:
        ex_type, ex_val, _ = sys.exc_info()
        exception_msg = f'【错误报告】\n检测力扣竞赛时发生错误\n错误类型: {ex_type}\n错误值: {ex_val}'
        print(exception_msg)
    else:
        for contest in recentContests:
            textMsg = f"【力扣竞赛】\n<{contest[0]}\n竞赛时间: {contest[2]}>"
        

requestPayload = {"query":"\n    query questionOfToday {\n  todayRecord {\n    date\n    userStatus\n    question {\n      questionId\n      frontendQuestionId: questionFrontendId\n      difficulty\n      title\n      titleCn: translatedTitle\n      titleSlug\n      paidOnly: isPaidOnly\n      freqBar\n      isFavor\n      acRate\n      status\n      solutionNum\n      hasVideoSolution\n      topicTags {\n        name\n        nameTranslated: translatedName\n        id\n      }\n      extra {\n        topCompanyTags {\n          imgUrl\n          slug\n          numSubscribed\n        }\n      }\n    }\n    lastSubmission {\n      id\n    }\n  }\n}\n    ","variables":{},"operationName":"questionOfToday"}


def LeetcodeDaily() -> List:
    dailyUrl = 'https://leetcode.cn/graphql/'
    s = requests.Session()
    response = s.post(url=dailyUrl, headers=headers, json=requestPayload)
    response = json.loads(response.text)
    s.close()

    date = response['data']['todayRecord'][0]['date']
    question = response['data']['todayRecord'][0]['question']

    ans = [
        date, 
        False, 
        question['frontendQuestionId'], 
        question['titleCn'], 
        question['difficulty'],
        question['titleSlug']
    ]
    return ans

def CheckStatus() -> bool:
    #payload = json.dumps(requestPayload)

    dailyUrl = 'https://leetcode.cn/graphql/'
    s = requests.Session()
    response = s.post(url=dailyUrl, headers=headers, json=requestPayload)
    response = json.loads(response.text)
    s.close()

    if response['data']['todayRecord'][0]['userStatus'] == 'FINISH':
        return True
    else:
        return False

def CreateSolutionFile(name:str, title: str, chineseTitle: str):
    '''创建每日一题的文件

    Args:
        name (str): 文件名
    '''
    monthDir = datetime.now().strftime("%Y.%m")
    leetcodeBasePath = "/home/TDK/Projects/My-Leetcode/daily/"
    if not os.path.exists(os.path.join(leetcodeBasePath,monthDir)):
        os.makedirs(os.path.join(leetcodeBasePath,monthDir))
    
    solutionPath = os.path.join(leetcodeBasePath, monthDir, f"{name}.py")
    timeStr = datetime.now().strftime('%Y-%m-%d')
    with open(solutionPath, "w+") as f:
        
        preContent = f'"""\n日期: {timeStr}\n题目: {chineseTitle}\n链接: https://leetcode.cn/problems/{title}/\n"""\n\nfrom typing import *\nfrom collections import *\nfrom leetcode_utils import *\n'
        content = GetSolutionContent(title)
        testcase = GetSolutionTestCase(title)
        
        f.write(preContent + content + testcase)

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
        headers=headers,
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
        "query": "query questionData($titleSlug: String!) {\n  question(titleSlug: $titleSlug) {\n    codeSnippets {\n      lang\n      langSlug\n      code\n      __typename\n    }\n}\n}\n"
    }
    url = "https://leetcode.cn/graphql/"

    res:requests.Response = requests.post(
        url=url,
        headers=headers,
        json=payload
    )

    content = ""
    if res.status_code == 200:
        
        res = res.json()
        codeSnippet = res["data"]["question"]["codeSnippets"]
        for i in codeSnippet:
            if i["lang"] == "Python3":
                content = i["code"]
                break
    else:
        print("失败")
        
    return content
    

daily_file_path = "/home/TDK/Projects/My-Leetcode/bot/LeetcodeDaily.json"    

def InitialDaily():
    
    with open(daily_file_path, 'w+') as f:
        
        q = LeetcodeDaily()
        
        json.dump(q, f)

        # 创建任务
        timeStr = datetime.now().strftime('%Y-%m-%d')
        dailyURL = f'https://leetcode.cn/problems/{q[5]}'
        
        # 创建文件
        CreateSolutionFile(f"{q[2]}.{q[5]}", q[5], q[3])

def InitialDailyTest():
    with open(daily_file_path, 'w+') as f:
        
        q = LeetcodeDaily()
        
        json.dump(q, f)
        
        # 创建文件
        CreateSolutionFile(f"{q[2]}.{q[5]}", q[5], q[3])

if __name__ == "__main__":
    CheckContests()
