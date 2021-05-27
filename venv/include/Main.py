from jira import JIRA
from prettytable import PrettyTable
import getpass
import time

server = input("server address:")
username = input("username:")
passwd = getpass.getpass(prompt="password:")

print('\r')
print("当前用户: \033[1;35m", username, "\033[0m!")

jira = JIRA(server, basic_auth=(username, passwd))

projectTable = PrettyTable(["Key", " 名称 ", "name"])
projectTable.align = "l"
for project in jira.projects():
    projectTable.add_row([project.key, project.name, project.id])
print(projectTable)

def searchIssueWithKey(key):
    today = time.strftime("%Y-%m-%d", time.localtime(time.time()))
    # issues1 = jira.search_issues('project = ' + key + ' AND created >= ' + today + ' AND reporter = currentUser()')
    issues1 = jira.search_issues('project = ' + key + ' AND created >= ' + today + ' AND reporter = 贾国强（测试）')
    print('\r')
    print("当前用户今天所提bug总数：", issues1.total)
    table1 = PrettyTable(["Key", " 状态 ", "处理人", "描述"])
    table1.align = "l"
    for issue in issues1:
        table1.add_row([issue.key, issue.fields.status.name, issue.fields.assignee.displayName, issue.fields.summary])

    print(table1)
    projectKey = input("请输入要查询的项目的key：")
    searchIssueWithKey(projectKey)

projectKey = input("请输入要查询的项目的key：")
searchIssueWithKey(projectKey)


